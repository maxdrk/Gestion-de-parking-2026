# Gestion de parking

Petit MVP en Python pour gérer les entrées, les sorties et le paiement des tickets d'un parking. Les données sont stockées localement dans une base SQLite (`tickets.db`).

## Lancer l'application

Depuis la racine du projet :

- **Windows** : exécuter `run_env.ps1` dans PowerShell.
- **Linux/macOS** : exécuter `bash run_env.sh`.

Les scripts créent un environnement virtuel, installent la dépendance (`pandas`) puis démarrent l'application. On peut aussi lancer `python main.py` après avoir installé les dépendances.

## Utilisation

Dans le menu principal, choisir :

1. **Entrer** : créer un ticket à l'arrivée du véhicule.
2. **Payer** : saisir la référence du ticket pour calculer et confirmer le paiement.
0. **Quitter** : fermer l'application.

Dans le menu des tickets, on peut enregistrer la sortie d'un véhicule ou afficher les tickets enregistrés.

## Tarification du MVP

Les 30 premières minutes sont gratuites. Ensuite, chaque tranche commencée de 15 minutes coûte 0,30 €, avec un maximum de 12 €.
