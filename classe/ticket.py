from parking import Parking
from sql import SQL
from tkinter import messagebox

class Ticket:

    def __init__(self):
        self.__parking = Parking()
        self.__sql = SQL()

    def enter(self):
        if self.__parking.verifCapacity():
            command = self.__sql.Command(  "INSERT INTO tickets DEFAULT VALUES")
            if isinstance(command, Exception):
                print(f"Erreur lors de la génération du ticket : {command}")
                return None
            ticketId = command.lastrowid
            messagebox.showinfo("succès",f"Ticket généré avec succès \n numéro : {ticketId}")
            return ticketId
        else:
            print("Parking complet")
            return None

    def getId(self, ticketId):
        return self.__sql.Command("SELECT id, heure_entree, heure_sortie FROM tickets WHERE id = ?",(ticketId,)).fetchone()

    def ObtenirTicket(self, ticketId):
        ticket = self.getId(ticketId)
        if ticket is None:
            print("Aucun ticket trouvé pour cet ID.")
            return None

        if ticket[2] is not None:
            print("Ce ticket a déjà été clôturé.")
            return None

        return ticket