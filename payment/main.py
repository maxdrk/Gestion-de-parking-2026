import sqlite3
import payment.getTicket as getTicket

def initSql():
    connexion = sqlite3.connect("tickets.db")
    connexion.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            heure_entree TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
            heure_sortie TEXT,
            prix float,
            paid_tickets boolean
        )
    """)
    return connexion

def init():
    connexion = initSql()
    try:
        while True:
            ticket_id = int(input("Pour quel ticket voulez-vous sa durée :"))
            getTicket.getTickets(connexion=connexion, id=ticket_id)
            back = str(input("Revenir au menu ? Y/N")).lower()
            if back == "y":
                break
    finally:
        connexion.close()
