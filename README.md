# Gestion de parking

## Présentation du projet

Ce projet consiste en un MVP développé en Python permettant de gérer manuellement les entrées, les sorties et les paiements des tickets d'un parking.

Les données sont stockées localement dans une base de données SQLite (`tickets.db`).

L'application a été conçue pour fonctionner sans borne automatisée. Toutes les opérations sont effectuées manuellement par l'intermédiaire de l'interface en ligne de commande.

## Lancement de l'application

Depuis la racine du projet, plusieurs possibilités permettent de démarrer l'application :

- **Windows** : exécuter le script `run_env.ps1` dans PowerShell.
- **Linux / macOS** : exécuter le script `run_env.sh`.
- **Manuellement** : installer les dépendances nécessaires, puis lancer `python main.py`.

Les scripts de lancement se chargent de créer un environnement virtuel, d'installer la dépendance `pandas` et de démarrer l'application.

## Utilisation

L'application propose un menu principal permettant d'accéder aux différentes fonctionnalités :

1. **Entrer** : permet d'accéder au menu de gestion des tickets, qui propose les opérations suivantes :
   - Enregistrer l'entrée d'un véhicule.
   - Enregistrer la sortie d'un véhicule.
   - Consulter l'ensemble des tickets enregistrés, avec leurs heures d'entrée et de sortie ainsi que leur statut de paiement.

2. **Payer** : permet de saisir la référence d'un ticket afin de calculer le montant dû et de confirmer son paiement.

3. **Quitter** : ferme l'application.

Le menu de gestion des tickets centralise ainsi les opérations liées au suivi des véhicules présents dans le parking.

## Tarification du MVP

Le calcul du tarif repose sur les règles suivantes :

- Les 30 premières minutes de stationnement sont gratuites.
- Au-delà de cette période, chaque tranche de 15 minutes entamée est facturée 0,30 €.
- Le montant total est plafonné à 12 €.