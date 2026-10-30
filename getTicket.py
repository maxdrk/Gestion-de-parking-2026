import datetime
import math

def getTickets(connexion, id):

    ticket = connexion.execute(
        """
        SELECT heure_entree, heure_sortie FROM tickets WHERE id = ?""",(id,)
    ).fetchone()

    if ticket is None:
        print("Aucun ticket existant pour cette référence.")
        return None
    heure_entree, heure_sortie = ticket

    if heure_sortie is None:
        print("Ce ticket est toujours ouvert.")
        return None
    
    entree = datetime.datetime.fromisoformat(heure_entree)
    sortie = datetime.datetime.fromisoformat(heure_sortie)
    duree = sortie - entree
    duree_minutes = duree.total_seconds() / 60

    print(f"Durée du stationnement : {duree}")
    minutes_facturables = max(0, duree_minutes - 30)
    tranches = math.ceil(minutes_facturables / 15)
    total = tranches * 0.30
    total = min(total, 12)

    print(f"Montant à payer : {total:.2f} €")

    confirmation = input(
        "Confirmer le paiement ? (Y/N) : "
    ).strip().lower()

    if confirmation == "y":
        connexion.execute("""UPDATE tickets SET paid_ticket = 1 WHERE id = ?""",(id,))
        connexion.commit()
        print("Paiement confirmé.")
        return total

    print("Paiement annulé.")
    return None