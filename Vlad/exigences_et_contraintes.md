
### Profils utilisateurs (acteurs)
| Acteur | Description | Rôle dans le système |
|---|---|---|
| **Régie des Parkings** | Organisation responsable de l'exploitation du parking et commanditaire du projet. | Supervision générale de l'activité du parking et suivi de son fonctionnement. |
| **Agent d'accueil** | Employé présent du lundi au vendredi, de 07h00 à 19h00. | Consultation des informations relatives aux entrées, aux sorties, aux paiements et aux abonnements via l'interface de supervision. |
| **Client** | Personne utilisant le parking pour stationner son véhicule. | Entrée et sortie du parking, paiement du stationnement via les bornes automatiques. |
| **Abonné** | Client disposant d'un abonnement au parking. | Utilisation du parking dans le cadre de son abonnement et selon sa validité. |



## Exigences fonctionnelles
### Vue d'ensemble

| ID | Fonctionnalité | Description |
|---|---|---|
| EF-01 | Supervision du parking | Le système doit afficher en temps réel les informations relatives à l'activité du parking. |
| EF-02 | Gestion des accès | Le système doit gérer les entrées et les sorties des véhicules. |
| EF-03 | Paiement du stationnement | Le système doit permettre aux clients de payer leur stationnement via des bornes automatiques, y compris sans connexion Internet. |
| EF-04 | Suivi des passages | Le système doit enregistrer et permettre de consulter les entrées et les sorties des véhicules. |
| EF-05 | Suivi des paiements | Le système doit permettre de consulter l'état des paiements effectués par les clients. |
| EF-06 | Gestion des abonnés | Le système doit permettre la gestion et le suivi des abonnements au parking. |

### Description détaillée des fonctionnalités

#### EF-01 — Supervision du parking
Le système doit proposer une interface de supervision permettant de consulter en temps réel 
- Les entrées et les sorties des véhicules.
- L'état des paiements.
- Les informations relatives aux abonnements.

#### EF-02 — Gestion des accès
Le système doit assurer la gestion des entrées et des sorties des véhicules du parking.
Cette fonctionnalité doit rester opérationnelle même en cas d'interruption de la connexion Internet.

#### EF-03 — Paiement du stationnement
Le système doit permettre aux clients d'effectuer le paiement de leur stationnement à l'aide des bornes automatiques.
Les fonctions de paiement doivent rester disponibles en cas de perte de connexion Internet, selon les modalités techniques à confirmer avec le client.

#### EF-04 — Suivi des passages
Le système doit permettre l'enregistrement et la consultation des passages des véhicules.
Les informations suivies comprennent :
- La date et l'heure d'entrée.
- La date et l'heure de sortie.
- Les informations permettant d'associer les passages au ticket ou à l'abonnement concerné.

#### EF-05 — Suivi des paiements
Le système doit permettre au personnel autorisé de consulter les informations relatives aux paiements du stationnement.
Il doit notamment permettre de connaître l'état des paiements associés aux tickets.

#### EF-06 — Gestion des abonnés
Le système doit permettre la gestion et le suivi des abonnés du parking.
Il doit permettre de consulter les informations relatives aux abonnements et à leur période de validité.


## Exigences non fonctionnelles (ENF)

- **ENF-01 : Fonctionnement hors ligne**  
  Le système doit continuer à assurer ses fonctions principales (entrées, sorties et paiements) même en cas de perte de connexion Internet.

- **ENF-02 : Interface utilisateur**  
  L'interface doit être simple, claire et intuitive afin de faciliter son utilisation par le personnel chargé de l'exploitation du parking.

**ENF-03 — Conservation des données**
Le système doit conserver localement les données nécessaires au fonctionnement du parking, y compris pendant une interruption de la connexion Internet.
Les modalités de conservation et de sauvegarde des données sont à confirmer avec le client.

**ENF-04 — Sécurité des données**
Le système doit protéger les informations relatives aux clients, aux abonnés et aux paiements.
L'accès aux informations de gestion doit être réservé aux personnes autorisées.
Les modalités d'authentification et les différents niveaux d'autorisation sont à confirmer avec le client.

**ENF-05 — Reprise après interruption**
Après le rétablissement de la connexion Internet, le système doit continuer à fonctionner sans perte des opérations enregistrées localement.
Si une synchronisation avec des services externes est nécessaire, elle doit permettre d'éviter les pertes et les doublons de données.
Les modalités techniques sont à confirmer avec le client.

**ENF-06 — Disponibilité du système**
Le système doit être adapté au fonctionnement continu du parking, ouvert 24h/24 et 7j/7.
Les objectifs de disponibilité et les procédures de récupération après une panne technique sont à confirmer avec le client.


### Minimum Viable Product (MVP)
Les fonctionnalités essentielles proposées pour le MVP sont :

- Gestion des entrées et des sorties.
- Paiement via les bornes automatiques.
- Fonctionnement local sans connexion Internet.
- Suivi des passages et des paiements.
- Interface de supervision.
- Gestion des abonnements.

# Contraintes
- **C_1 :** Le parking fonctionne 24 heures sur 24, 7 jours sur 7.
- **C_2 :** Le parking dispose de 220 places de stationnement.
- **C_3 :** Un agent d'accueil est présent du lundi au vendredi, de 7h00 à 19h00. En dehors de ces horaires, le parking doit fonctionner de manière entièrement automatisée, sans intervention du personnel.


# Questions ouvertes
## Gestion des accès — EF-02

| ID | Question | Statut |
|---|---|---|
| Q-01 | Comment le système doit-il identifier les véhicules ou les tickets à l'entrée et à la sortie ? | À clarifier |
| Q-02 | Quelles conditions permettent l'ouverture de la barrière ? | À clarifier |
| Q-03 | Que doit faire le système lorsque les 220 places sont occupées ? | À clarifier |
| Q-04 | Comment les abonnés doivent-ils accéder au parking ? | À clarifier |
| Q-05 | Quelle procédure appliquer en cas de panne du système de contrôle d'accès ? | À clarifier |

## Paiements — EF-03 et EF-05
| ID | Question | Statut |
|---|---|---|
| Q-06 | Quels moyens de paiement doivent être acceptés ? | À clarifier |
| Q-07 | Comment les paiements par carte doivent-ils être gérés en l'absence de connexion Internet ? | À clarifier |
| Q-08 | Que doit-il se passer lorsqu'un paiement est refusé ou interrompu ? | À clarifier |
| Q-09 | Le système doit-il permettre une clôture de caisse et la consultation de rapports financiers ? | À clarifier |

## Gestion des abonnés — EF-06
| ID | Question | Statut |
|---|---|---|
| Q-10 | Quels types d'abonnements sont proposés ? | À clarifier |
| Q-11 | Qui peut créer, modifier, renouveler ou annuler un abonnement ? | À clarifier |
| Q-12 | Que doit-il se passer lorsqu'un abonnement expire ? | À clarifier |

## Supervision — EF-01
| ID | Question | Statut |
|---|---|---|
| Q-13 | Le système doit-il afficher le nombre de places disponibles en temps réel ? | À clarifier |
| Q-14 | Quelles informations doivent apparaître sur le tableau de bord principal ? | À clarifier |
| Q-15 | Quels utilisateurs doivent avoir accès à l'interface de supervision ? | À clarifier |

## Fonctionnement local et sécurité — ENF
| ID | Question | Statut |
|---|---|---|
| Q-16 | Quelle durée d'autonomie est attendue en cas de coupure Internet ? | À clarifier |
| Q-17 | Une synchronisation avec des services externes est-elle nécessaire après le rétablissement de la connexion ? | À clarifier |
| Q-18 | Quelle procédure doit être appliquée en cas de panne du serveur local ? | À clarifier |
| Q-19 | Quelle fréquence de sauvegarde des données est attendue ? | À clarifier |
| Q-20 | Quelles règles d'authentification et de gestion des droits d'accès sont nécessaires ? | À clarifier |

## Budget et planning
| ID | Question | Statut |
|---|---|---|
| Q-21 | Quel budget est disponible pour le projet ? | À clarifier |
| Q-22 | Quels équipements existants doivent être conservés ou remplacés ? | À clarifier |
| Q-23 | Quelle est la date de livraison souhaitée ? | À clarifier |
| Q-24 | Quelles fonctionnalités sont indispensables pour la première version (MVP) ? | À clarifier |
| Q-25 | Qui sera responsable de la maintenance après le déploiement ? | À clarifier |


# Budget
Le budget alloué au développement et au déploiement de la nouvelle solution n'a pas encore été communiqué par le client.
Le projet vise notamment à réduire les pertes financières liées aux interruptions de service.
En mars 2026, une coupure Internet de 48 heures a entraîné une perte d'exploitation estimée à 6 000 €.
Les éléments budgétaires suivants restent à préciser :

- Le budget total disponible pour le projet.
- Le coût du développement de l'application.
- Les coûts de maintenance et de support.

**Statut : À confirmer avec le client.**


# 6. Livrables et planning
## 6.1 Livrables
Les livrables prévus dans le cadre du projet Gestion de parkings Valmont sont les suivants :
| ID | Livrable | Description |
|---|---|---|
| L-01 | Cahier des charges (CdC) | Document présentant le contexte, les besoins, les exigences et les contraintes du projet. |
| L-02 | Modélisation UML | Diagrammes permettant de représenter la structure et le fonctionnement du système. |
| L-03 | Démonstration du MVP | Première version fonctionnelle du système, présentée sur GitHub. |
| L-04 | Spécifications | Description détaillée des fonctionnalités et des choix de conception. |
| L-05 | Démonstration du projet | Présentation de l'avancement et des fonctionnalités réalisées. |
| L-06 | Tests | Vérification du fonctionnement du système, notamment en cas de perte de connexion Internet. |
| L-07 | Démonstration client et mise en production | Présentation finale au client et mise en production selon les modalités convenues. |

## 6.2 Échéances
| Étape | Échéance prévisionnelle |
|---|---|
| Choix du sujet | Semaine du 05/10/2026 |
| Cahier des charges | Semaine du 12/10/2026 |
| Modélisation UML | Semaine du 19/10/2026 |
| Démonstration du MVP sur GitHub | Semaine du 02/11/2026 |
| Spécifications | Semaines du 09/11 et du 16/11/2026 |
| Démonstration du projet | Semaine du 23/11/2026 |
| Tests | Semaine du 30/11/2026 |
| Démonstration client et mise en production | Semaine du 07/12/2026 |

## 6.3 Retours vers le client
Des échanges avec Monsieur Jean-Luc Bertrand, directeur d'exploitation, sont prévus afin de clarifier les besoins et de valider les différentes étapes du projet.

Ces échanges permettront notamment de :
- Clarifier les exigences fonctionnelles et non fonctionnelles.
- Confirmer les modalités de fonctionnement hors ligne.
- Vérifier que les fonctionnalités proposées correspondent aux besoins du parking.
- Présenter les résultats des différentes étapes de développement.
- Recueillir les remarques du client et adapter les spécifications si nécessaire.
- Préparer la validation finale du projet.

Les questions en attente de réponse sont répertoriées dans la section « Questions ouvertes ».
Les dates des échanges et les décisions prises seront consignées dans les annexes du cahier des charges.


# Glossaire
| Terme | Définition |
|---|---|
| Cloud | Infrastructure informatique distante accessible via Internet. |
| Infrastructure locale | Ensemble des équipements et services informatiques hébergés sur le site du parking ou dans son infrastructure interne. |
| Hors ligne (Offline) | Mode de fonctionnement sans connexion Internet. |
| Interface de supervision | Interface permettant de consulter et de suivre les informations relatives au fonctionnement du parking. |
| Borne automatique | Équipement permettant aux clients d'effectuer certaines opérations sans intervention du personnel. |
| Abonné | Client disposant d'un abonnement au parking. |
| MVP | Minimum Viable Product : première version du produit contenant les fonctionnalités essentielles. |
| Exigence fonctionnelle (EF) | Fonction ou service que le système doit fournir. |
| Exigence non fonctionnelle (ENF) | Exigence concernant les caractéristiques de fonctionnement du système, telles que la sécurité, la disponibilité ou la performance. |
| Synchronisation | Processus permettant de mettre en cohérence des données conservées dans plusieurs systèmes. |
| Cahier des charges | Document définissant les besoins, les exigences et les contraintes d'un projet. |


