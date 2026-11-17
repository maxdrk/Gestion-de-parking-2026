from parking import Parking
from sql import SQL
from tkinter import messagebox
from datetime import datetime
from tkinter import simpledialog

class Ticket:

    def __init__(self):
        self.__parking = Parking()
        self.__sql = SQL()

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
    def sortie(self):
        ticketId = simpledialog.askinteger(title="Numéro du ticket",prompt="Quel est le numéro du ticket à clôturer ?")
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