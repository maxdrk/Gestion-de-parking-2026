import json
import pandas as pd
from io import StringIO


def FormatJson(connexion):
    cursor = connexion.execute("SELECT id as référence,heure_entree as arrivée, heure_sortie as sortie FROM tickets")
    colonnes = [description[0] for description in cursor.description]
    lignes = cursor.fetchall()

    data = [dict(zip(colonnes, ligne)) for ligne in lignes]
    return json.dumps(data, ensure_ascii=False, indent=4)


def toPandas(connexion):
    json_data = FormatJson(connexion)
    dataframe = pd.read_json(StringIO(json_data))
    print(dataframe)
    return dataframe