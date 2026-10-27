# Gestion des entrées et sorties du parking

## Présentation

Cette fonctionnalité gère le passage des véhicules dans un parking : un ticket est créé à l'entrée, puis retrouvé à la sortie à l'aide de sa référence. Les données sont stockées localement dans une base SQLite.

## Objectif

Permettre de :

- créer un ticket lors de l'entrée d'un véhicule ;
- associer au ticket une référence unique et l'heure d'entrée ;
- retrouver le ticket à la sortie à partir de sa référence ;
- enregistrer l'heure de sortie ;
- consulter les stationnements en cours et l'historique.

## Technologies envisagées

- **SQLite** : stockage local des tickets et des heures de passage ;
- **Pandas** : éventuellement pour analyser les données, produire des tableaux ou des rapports. Il n'est pas nécessaire pour les opérations de stockage de base.

Le langage, l'interface et le mode de saisie ou de lecture des références restent à confirmer selon le cahier des charges.

## Données d'un ticket

| Champ | Description |
|---|---|
| `id` | Identifiant unique du ticket, utilisé pour le retrouver à la sortie |
| `heure_entree` | Date et heure de création du ticket |
| `heure_sortie` | Date et heure de sortie ; vide tant que le véhicule est dans le parking |

## Parcours prévu

1. À l'entrée, générer ou saisir une référence unique et enregistrer l'heure d'entrée.
2. À la sortie, rechercher le ticket par sa référence.
3. Si le ticket existe et n'a pas encore de sortie, enregistrer l'heure de sortie.
4. Permettre de consulter les tickets encore actifs et l'historique des tickets terminés.

## Première version (MVP)

- Créer la base SQLite et la table des tickets.
- Implémenter l'enregistrement d'une entrée.
- Implémenter la sortie à partir d'une référence.
- Afficher les stationnements en cours et l'historique.
- Gérer les erreurs courantes : référence inconnue, référence déjà utilisée ou ticket déjà clôturé.

## Points à confirmer

- La référence est-elle imprimée ou générée automatiquement par le système ?
- Comment la référence est-elle fournie à la sortie : saisie, lecture optique ou autre ?
- L'heure est-elle toujours horodatée automatiquement ?
- Faut-il gérer le nombre de places disponibles, calculer un tarif ou produire des exports ?
- Quelles contraintes de conservation et de format des dates le client impose-t-il ?

## Développement

Travailler sur une branche dédiée, par exemple `feature/parking-entrees-sorties`. Tester le parcours complet entrée → recherche par référence → sortie avant de proposer les changements à fusionner dans `main`.
