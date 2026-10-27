import enter
import sqlite3


with sqlite3.connect("tickets.db") as connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            heure_entree TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            heure_sortie TEXT
        )
    """)


print("Test de génération d'entrée")
enter.creation_ticket(connection=connection)
