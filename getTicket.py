import datetime

# Prévoir un système boolen pr vérifier les paiements
def getTickets(connexion,id):

    ticket = connexion.execute(("""select heure_entree as arrivee, heure_sortie as sortie from tickets where id = ?"""),(id,)).fetchone()
    if ticket:
        if ticket is None:
            print('Aucun ticket existant pour cette référence')
            return None
    heure_entree, heure_sortie = ticket

    if heure_sortie is None:
        print("Ce ticket est toujours ouvert : il n'a pas encore d'heure de sortie.")
        return None

    entree = datetime.datetime.fromisoformat(heure_entree)
    sortie = datetime.datetime.fromisoformat(heure_sortie)
    duree = sortie - entree

    print(f"Durée du stationnement : {duree}")
    return duree