# Gestion de parking 2026

MVP en Python pour gérer les entrées, les sorties et le paiement des tickets d'un parking. Les données sont stockées localement dans une base SQLite (`tickets.db`), créée automatiquement au premier lancement.

> Présentation du projet : [wiki](https://github.com/maxdrk/Gestion-de-parking-2026/wiki)

---

## Lancer l'application

Les scripts se lancent **depuis la racine du projet** :

```Windows
.\run_env.ps1        # PowerShell
```

```Linux / macOS
bash run_env.sh      # Bash
```

Ils créent un environnement virtuel, installent les dépendances (`pandas`, `pandastable`, `textual`), puis démarrent la version console.

Si les dépendances sont déjà installées, on peut lancer directement depuis la racine :

- `python main_cli.py` : version console
- `python main_gui.py` : interface graphique (Tkinter)
- `python main_tui.py` : interface terminal (Textual)

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
├── main_cli.py            ← version console
├── main_gui.py            ← interface graphique
├── main_tui.py            ← interface terminal
├── requirements.txt
├── run_env.ps1
├── run_env.sh
├── docs/
│   ├── Cahier des charges/
│   ├── Diagrammes/
│   └── Use Case/
├── classe/                ← code partagé par les interfaces
│   ├── sql.py             ← connexion à la base de données
│   └── parking.py         ← gestion des places
├── cli/
│   ├── tickets/           ← entrées, sorties, affichage
│   └── payment/           ← calcul et confirmation du paiement
├── gui/
│   ├── gui.py
│   └── ticket.py
└── tui/
    ├── tui.py
    └── tui.tcss
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
  - Vladyslav -> OK
- **MVP entrée / sortie / paiement** : terminé

**Répartition du cahier des charges** (sur base du [template EPHEC](https://moodle.ephec.be/pluginfile.php/1111827/mod_resource/content/0/Cahier%20des%20Charges%20-%20Template.pdf)) :

- **Maxime** et **Liam** : parties 1 à 3 (non incluse)
- **Gregory** et **Vladyslav** : parties 3 à 6

## Usage de l'IA

*L'IA Claude Opus 5.5 (Anthropic), en effort moyen, a été utilisée pour aider à la mise en forme de ce README.*

---

© Maxime Derick, Gregory Kabasele, Liam Bruyère, Vladyslav Volodichev
