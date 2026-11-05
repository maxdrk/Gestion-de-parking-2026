import json
import sqlite3
import pandas as pd
from io import StringIO



connection = sqlite3.connect("tickets.db")
connection.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        heure_entree TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
        heure_sortie TEXT,
        paid_ticket boolean
    )
""")

def FormatJson(connexion):
    cursor = connexion.execute("SELECT id as référence,heure_entree as arrivée, heure_sortie as sortie, paid_ticket as payé FROM tickets")
    colonnes = [description[0] for description in cursor.description]
    lignes = cursor.fetchall()
    data = [dict(zip(colonnes, ligne)) for ligne in lignes]
    return json.dumps(data, ensure_ascii=False, indent=4)


def toPandas(connexion):
    json_data = FormatJson(connexion)
    dataframe = pd.read_json(StringIO(json_data))
    print(dataframe)
    return dataframe

