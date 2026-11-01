import datetime
from payment import calc_amount


def getTickets(connexion, id):
    ticket = connexion.execute("""
        SELECT heure_entree, heure_sortie, paid_ticket
        FROM tickets
        WHERE id = ?
    """, (id,)).fetchone()

    if ticket is None:
        print("Aucun ticket existant pour cette référence.")
        return None

    heure_entree, heure_sortie, paid_ticket = ticket

    if paid_ticket == 1:
        print("Ce ticket est déjà payé.")
        return None

    if heure_sortie is None:
        print("Ce ticket est toujours ouvert.")
        return None

    entree = datetime.datetime.fromisoformat(heure_entree)
    sortie = datetime.datetime.fromisoformat(heure_sortie)

    duree = sortie - entree

    total = calc_amount(entree, sortie)

    print(f"Durée du stationnement : {duree}")
    print(f"Montant à payer : {total:.2f} €")

    confirmation = input(
        "Confirmer le paiement ? (Y/N) : "
    ).strip().lower()

    if confirmation == "y":
        connexion.execute("""
            UPDATE tickets
            SET prix = ?, paid_ticket = 1
            WHERE id = ?
        """, (total, id))

        connexion.commit()

        print("Paiement confirmé.")
        return total

    print("Paiement annulé.")
    return None
