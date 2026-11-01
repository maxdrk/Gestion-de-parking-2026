from datetime import datetime, timedelta

free_minutes = 30
day_quarter_cents = 30
night_cents = 300
cap_24h_cents = 1200


def calc_amount(entree, sortie):
    if not isinstance(entree, datetime) or not isinstance(sortie, datetime):
        raise TypeError("entree et sortie doivent etre des objets datetime.")

    if entree.utcoffset() is not None or sortie.utcoffset() is not None:
        raise ValueError("Utilisez les dates locales sans fuseau de tickets.db.")

    if sortie < entree:
        raise ValueError("La sortie ne peut pas etre avant l'entree.")

    duration = sortie - entree

    if duration <= timedelta(minutes=free_minutes):
        return 0.0

    current = entree + timedelta(minutes=free_minutes)
    period_end = entree + timedelta(hours=24)

    amount = 0
    period_amount = 0
    paid_night_end = None

    while current < sortie:
        if current >= period_end:
            amount += min(period_amount, cap_24h_cents)
            period_amount = 0
            period_end += timedelta(hours=24)

        if 7 <= current.hour < 19:
            period_amount += day_quarter_cents

            night_start = current.replace(
                hour=19, minute=0, second=0, microsecond=0
            )

            current = min(
                current + timedelta(minutes=15),
                night_start,
                period_end,
                sortie
            )

        else:
            morning = current.replace(
                hour=7, minute=0, second=0, microsecond=0
            )

            if current.hour >= 19:
                morning += timedelta(days=1)
            if morning != paid_night_end:
                period_amount += night_cents
                paid_night_end = morning
            current = min(
                morning,
                period_end,
                sortie
            )

    amount += min(period_amount, cap_24h_cents)
    return amount / 100

if __name__ == "__main__":
    entree = datetime(2026, 10, 30, 10, 0)
    sortie = datetime(2026, 10, 31, 11, 0)
    print(calc_amount(entree, sortie))
