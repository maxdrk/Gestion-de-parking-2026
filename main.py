import sqlite3
import getTicket

with sqlite3.connect("tickets.db") as connexion:
    connexion.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            heure_entree TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
            heure_sortie TEXT,
            prix REAL,
            paid_ticket INTEGER NOT NULL DEFAULT 0
        )
    """)

    while True:
        try:
            ticket_id = int(input("Entrez l'ID du ticket : "))

            if ticket_id <= 0:
                print("L'ID doit être un nombre positif.")
                continue

            break

        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    getTicket.getTickets(connexion, ticket_id)