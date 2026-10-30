import sqlite3
import getTicket

with sqlite3.connect("tickets.db") as connexion:
    connexion.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            heure_entree TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
            heure_sortie TEXT,
            paid_tickets boolean
        )
    """)

id = int(input("Pour quel ticket voulez-vous sa durée :"))

getTicket.getTickets(connexion=connexion,id=id)