from classe.parking import Parking
from classe.sql import SQL
from tkinter import messagebox
from datetime import datetime
from tkinter import simpledialog
import json
import pandas as pd
from io import StringIO
import math

class Ticket:

    def __init__(self):
        self.__parking = Parking()
        self.__sql = SQL()
        self.toPandas()

    def enter(self):
        if self.__parking.verifCapacity():
            command = self.__sql.Command(  "INSERT INTO tickets DEFAULT VALUES")
            if isinstance(command, Exception):
                messagebox.showerror("Erreur",f"Erreur lors de la génération du ticket : {command}")
                return None
            ticketId = command.lastrowid
            messagebox.showinfo("succès",f"Ticket généré avec succès \n numéro : {ticketId}")
            return ticketId
        else:
            messagebox.showerror("Erreur","Parking complet")
            return None
    def sortie(self,ticketId):
        #ticketId = simpledialog.askinteger(title="Numéro du ticket",prompt="Quel est le numéro du ticket à clôturer ?")
        if ticketId is None:
            return
        ticket = self.ObtenirTicket(ticketId)
        if ticket is None:
            return
        heure_sortie = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = self.__sql.Command("UPDATE tickets SET heure_sortie = ? WHERE id = ?",(heure_sortie, ticketId))
        if isinstance(result, Exception): 
            messagebox.showerror("Erreur",f"Impossible de clôturer le ticket : {result}")
            return
        if result.rowcount == 0:
            messagebox.showerror( "Erreur","Aucun ticket n'a été modifié.")
            return
        messagebox.showinfo("Succès",f"Ticket {ticketId} clôturé avec succès !\n"f"Heure de sortie : {heure_sortie}")

    def getId(self, ticketId):
        return self.__sql.Command("SELECT id, heure_entree, heure_sortie FROM tickets WHERE id = ?",(ticketId,)).fetchone()

    def ObtenirTicket(self, ticketId):
        ticket = self.getId(ticketId)
        if ticket is None:
            messagebox.showerror("Erreur","Aucun ticket trouvé pour cet ID.")
            return None

        if ticket[2] is not None:
            messagebox.showinfo("Info","Ce ticket a déjà été clôturé.")
            return None

        return ticket

    def payer(self, ticketId=None):
        if ticketId is None:
            ticketId = simpledialog.askinteger(title="Numéro du ticket", prompt="Quel est le numéro du ticket à payer ?")
        if ticketId is None:
            return None

        ticket = self.__sql.Command("""SELECT heure_entree, heure_sortie, paid_ticket FROM tickets WHERE id = ?""", (ticketId,)).fetchone()
        if ticket is None:
            messagebox.showerror("Erreur", "Aucun ticket existant pour cette référence.")
            return None
            
        heure_entree, heure_sortie, paid_ticket = ticket
        if heure_sortie is None:
            messagebox.showinfo("Info", "Ce ticket est toujours ouvert (véhicule non sorti).")
            return None
            
        if paid_ticket == 1:
            messagebox.showinfo("Info", "Le ticket est déjà payé.")
            return None
            
        entree = datetime.fromisoformat(heure_entree)
        sortie = datetime.fromisoformat(heure_sortie)
        duree = sortie - entree
        duree_minutes = duree.total_seconds() / 60
    
        messagebox.showinfo("Info", f"Durée du stationnement : {duree}")
        minutes_facturables = max(0, duree_minutes - 30)
        tranches = math.ceil(minutes_facturables / 15)
        total = min(tranches * 0.30, 12)
    
        pay = messagebox.askyesno("Confirmation", f"Montant à payer : {total:.2f} €\nConfirmer le paiement ?")
        if pay:
            self.__sql.Command("""UPDATE tickets SET paid_ticket = 1 WHERE id = ?""", (ticketId,))
            messagebox.showinfo("Succès", "Paiement enregistré !")
             

    def FormatJson(self):
        cursor = self.__sql.Command("SELECT id as référence,heure_entree as arrivée, heure_sortie as sortie FROM tickets")
        colonnes = [description[0] for description in cursor.description]
        lignes = cursor.fetchall()
        data = [dict(zip(colonnes, ligne)) for ligne in lignes]
        return json.dumps(data, ensure_ascii=False, indent=4)

    def toPandas(self):
        cursor = self.__sql.Command(
            'SELECT id AS "référence", heure_entree AS "arrivée", heure_sortie AS "sortie" , paid_ticket as payé FROM tickets')
        colonnes = [description[0] for description in cursor.description]
        lignes = cursor.fetchall()
        self.dataframe = pd.DataFrame(lignes, columns=colonnes)

        if not self.dataframe.empty:
            col_id = self.dataframe.columns[0]
            self.dataframe[col_id] = pd.to_numeric(
                self.dataframe[col_id], errors="coerce"
            ).astype("Int64")

            col_sortie = self.dataframe.columns[2]
            self.dataframe[col_sortie] = self.dataframe[col_sortie].fillna("En cours")

            col_paye = self.dataframe.columns[3]

            valeurs = pd.to_numeric(self.dataframe[col_paye], errors="coerce")
            self.dataframe[col_paye] = valeurs.map({
                1: "Payé",
                0: "Pas payé",
            })

        return self.dataframe

