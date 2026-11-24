import sqlite3

class SQL:

    def __init__(self):
        self.__connection = sqlite3.connect("tickets.db")
        self.verifSql()
    def verifSql(self):
        self.__connection.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                heure_entree TEXT NOT NULL DEFAULT
                    (datetime('now', 'localtime')),
                heure_sortie TEXT,
                paid_ticket BOOLEAN DEFAULT FALSE
            )
        """)
        self.__connection.commit()
    def CloseSql(self):
        self.__connection.close()
    def Command(self, command: str, params=()):
        try:
            cursor = self.__connection.execute(command, params)
            self.__connection.commit()
            return cursor
        except sqlite3.Error as e:
            return e