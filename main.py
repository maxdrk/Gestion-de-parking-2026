import enter
import exit
import sqlite3
import Formjson


with sqlite3.connect("tickets.db") as connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            heure_entree TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            heure_sortie TEXT
        )
    """)


ticketCloture = int(input('ticket à cloturé :'))


print("Test de génération d'entrée")
enter.creation_ticket(connection=connection)


print('Test de fermeture de ticket')
exit.sortie_ticket(connection=connection,ticket_id=ticketCloture)

print ("Transformation des données pour affichage optimal")
Formjson.toPandas(connection)

