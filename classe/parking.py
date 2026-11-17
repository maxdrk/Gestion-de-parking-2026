class Parking:

    def __init__(self, sql, capacity=220):
        self.__sql = sql
        self.__capacity = capacity

    def verifCapacity(self):
        requete = """
            SELECT COUNT(*)
            FROM tickets
            WHERE heure_sortie IS NULL
        """
        response = self.__sql.Command(requete)
        if isinstance(response, Exception):
            return False
        places_occupees = response.fetchone()[0]
        return places_occupees < self.__capacity