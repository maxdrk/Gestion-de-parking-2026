# Gestion de parking 2026

MVP en Python pour gérer les entrées, les sorties et le paiement des tickets d'un parking. Les données sont stockées localement dans une base SQLite (`tickets.db`), créée automatiquement au premier lancement.

> Présentation du projet : [wiki](https://github.com/maxdrk/Gestion-de-parking-2026/wiki)

---

## Lancer l'application

Les scripts se lancent **depuis le dossier `src/`** :

```Windows
cd src
.\run_env.ps1        # PowerShell
```

```Linux / macOS
cd src
bash run_env.sh      # Bash
```

Ils créent un environnement virtuel, installent les dépendances (`pandas`), puis démarrent l'application.
Si les dépendances sont déjà installées, on peut aussi lancer directement `python main.py` depuis `src/`.

## Utilisation

**Menu principal**

- **1. Entrer / sortir** : ouvre le menu des tickets
- **2. Payer** : saisir le numéro du ticket pour calculer et confirmer le paiement
- **0. Quitter le programme**

**Menu des tickets**

- **1.** Introduire une entrée
- **2.** Introduire une sortie
- **3.** Afficher la base de données
- **0.** Revenir au menu principal

## Tarification du MVP

- Les 30 premières minutes sont gratuites.
- Ensuite, chaque quart d'heure commencé coûte 0,30 €.
- Maximum de 12 € par 24 h.

## Structure du projet

```
├── docs/
│   ├── Cahier des charges/
│   ├── Diagrammes/
│   └── Use Case/
└── src/
    ├── main.py            ← point d'entrée (menu principal)
    ├── requirement.txt
    ├── run_env.ps1
    ├── run_env.sh
    ├── tickets/           ← entrées, sorties, affichage
    └── payment/           ← calcul et confirmation du paiement
```

## Branches

- **`main`** : version stable.
- **`dev`** : intégration de nos fonctionnalités terminées.
- **`enter-exit`** : gestion des entrées et sorties.
- **`payment`** : paiement des tickets.

## Avancement

- **Cahier des charges** : terminé
- **Diagramme use case** : terminé
- **Diagramme de classes** : terminé
- **Diagrammes de séquence** : en cours
  - Maxime -> OK
  - Gregory -> OK
  - Liam -> OK
  - Vladyslav -> EN ATTENTE
- **MVP entrée / sortie / paiement** : terminé

**Répartition du cahier des charges** (sur base du [template EPHEC](https://moodle.ephec.be/pluginfile.php/1111827/mod_resource/content/0/Cahier%20des%20Charges%20-%20Template.pdf)) :

- **Maxime** et **Liam** : parties 1 à 3 (non incluse)
- **Gregory** et **Vladyslav** : parties 3 à 6

## Usage de l'IA

*L’IA Claude Opus 5.5 (Anthropic), en effort moyen, a été utilisée pour aider à la mise en forme de ce README..*

---

© Maxime Derick, Gregory Kabasele, Liam Bruyère, Vladyslav Volodichev
