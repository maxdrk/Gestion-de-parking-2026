# Conception du projet de gestion de parking 

## Etape 1 : Concevoir le cahier de charge (Fini)

| Nom | Partie |
| ----| ------ |
| Maxime | 1 - 3 (non-inclus) |
| Liam | 1 - 3 (non-inclus) |
| Greg | 3 - 6 |
| Vlad | 3 - 6 |

> sur Base de cette template <br> **https://moodle.ephec.be/pluginfile.php/1111827/mod_resource/content/0/Cahier%20des%20Charges%20-%20Template.pdf**


## Etape 2 : Concevoir les différents diagrammes (En cours)

- diagramme use case : voir wiki ( Fait  )
- diagramme de classe : voir wiki ( Fait )
- diagramme séquentielle  <br> - Maxime Ok <br> - Greg OK <br> - Liam OK <br> - Vlad X 

## MVP (Fini)

- fonction d'entrée et sortie du parking : Dans la branche enter-exit

### Branches

#### Enter-exit 

Cette branche contient tout le code concernant la gestion d'entrée et de sortie du parking.

- génération de ticket
- cloture d'un ticket 
- mise de ces tickets dans la base de données

Note : Revérifier le MVP suite à la conception du diagramme de classe nombreuse ajouts sont nécessaires

#### payment

Cette branche contient tout le code dédié au paiement de ticket. Pour le moment cela gère seulement la durée qu'un client a passé dans le parking. Le plan tarifaire reste encore à faire.

---


> Lien du wiki : https://github.com/maxdrk/Gestion-de-parking-2026/wiki
---
<footer>© Maxime Derick,Gregory kabasele,Liam bruyere,Vladyslav Volodichev</footer>



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
