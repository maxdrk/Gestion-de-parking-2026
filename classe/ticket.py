class Ticket:

    def __init__(self, parking, sql):
        self.__parking = parking
        self.__sql = sql

    def enter(self):
        if self.__parking.verifcapacity():
            command = self.__sql.Command(
                "INSERT INTO tickets DEFAULT VALUES"
            )
            if isinstance(command, Exception):
                print(f"Erreur lors de la génération du ticket : {command}")
                return None
            ticketId = command.lastrowid
            print(f"Ticket généré avec succès : {ticketId}")
            return ticketId
        else:
            print("Parking complet")
            return None
    def obtenirTicket(self,ticketId):
        command = self.__sql.command("SELECT id, heure_entree as arrivée, heure_sortie as sortie FROM tickets WHERE id = ?",
                (ticketId,))
        requete = self.__sql.Command(command)
        return requete.fetchone()

    def ObtenirTicket(self, ticketId):
        ticket = self.__sql.ObtenirTicket(ticketId)
        if ticket is None:
            print("Aucun ticket trouvé pour cet ID.")
            return
        if ticket[2] is not None:
            print("Ce ticket a déjà été clôturé.")
            return
            

