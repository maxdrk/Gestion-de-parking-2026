import sqlite3
import datetime
from datetime import datetime


def obtenir_ticket(connection, ticket_id):
    return connection.execute(
        "SELECT id, heure_entree, heure_sortie FROM tickets WHERE id = ?",
        (ticket_id,)
    ).fetchone()

def sortie_ticket(connection, ticket_id):
    ticket = obtenir_ticket(connection, ticket_id)
    if ticket is None:
        print("Aucun ticket trouvé pour cet ID.")
        return
    if ticket[2] is not None:
        print("Ce ticket a déjà été clôturé.")
        return
    heure_sortie = datetime.now().isoformat(timespec="seconds")
    connection.execute(
        "UPDATE tickets SET heure_sortie = ? WHERE id = ?",
        (heure_sortie, ticket_id)
    )
    connection.commit()
    print(f"Ticket {ticket_id} : entrée à {ticket[1]}, sortie à {heure_sortie}")
