import sqlite3


def creation_ticket(connection):
    try:
        cursor = connection.execute(
            "INSERT INTO tickets DEFAULT VALUES"
        )
        ticket_id = cursor.lastrowid
        connection.commit()

        print(f"Ticket généré avec succès : {ticket_id}")
        return ticket_id

    except sqlite3.Error as e:
        connection.rollback()
        print(f"Erreur lors de la génération du ticket : {e}")
        return None
    
