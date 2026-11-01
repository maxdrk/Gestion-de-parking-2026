import enter
import exit
import sqlite3
import Formjson


connection = sqlite3.connect("tickets.db")
connection.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        heure_entree TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
        heure_sortie TEXT,
        paid_ticket boolean
    )
""")


def script():
    while True:
        choix = int(input("""Que voulez faire ? 
        \n 1. Introduire une entrée 
        \n 2. Introduire une sortie 
        \n 3. Afficher la base de données
        \n 0. Fermer le programme 
        \n choix :"""))
        if choix == 1:
            enter.creation_ticket(connection=connection)
        elif choix == 2:
            ticket_id = int(input("pour quel ticket voulez-vous introduire une sortie :"))
            exit.sortie_ticket(connection=connection, ticket_id=ticket_id)
        elif choix == 3:
            Formjson.toPandas(connexion=connection)
        elif choix == 0:
            break
        else:
            print("Erreur : veuillez choisir une proposition valide")

def init():
    script()

def close():
    if connection is not None:
        connection.close()
