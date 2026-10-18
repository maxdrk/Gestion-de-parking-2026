
# Cahier des charges — Gestion de parkings Valmont

**Version :** V1

**Date :** 18/10/2026

**Auteurs :**

1. Maxime Derick
2. Gregory Kabasele
3. Liam Bruyère
4. Vladyslav Volodichev

**Statut :** Document de travail — à valider avec le client.

## Conventions d'identification

| Élément | Format | Exemple |
|---|---|---|
| Objectif | O-X | O-1 |
| Règle métier | RM-XX | RM-01 |
| Donnée | D-XX | D-01 |
| Exigence fonctionnelle | EF-XX | EF-01 |
| Exigence non fonctionnelle | ENF-XX | ENF-01 |
| Contrainte | C-XX | C-01 |
| Question ouverte | Q-XX | Q-01 |
| Livrable | L-XX | L-01 |
| Critère de validation | V-XX | V-01 |

# 1. Contexte

## 1.1. Présentation du client

- **Client** : la Régie des Parkings Valmont, représentée par M. Jean-Luc Bertrand, directeur d'exploitation.
- **Activité** : exploitation d'un parking public de 220 places (RM-02), ouvert 24h/24 et 7j/7 (RM-01). Un agent d'accueil est présent du lundi au vendredi de 7h00 à 19h00 (RM-03). En dehors de ces heures (soirées, week-ends, jours fériés), le parking fonctionne de manière entièrement automatisée grâce aux bornes et aux caisses automatiques (RM-04).
- **Enjeux métier** : la Régie doit garantir l'accès au parking et l'encaissement des paiements en permanence, souvent sans personnel sur place. Toute interruption du système bloque les clients horaires et les abonnés, et prive la Régie de ses recettes.

## 1.2. Présentation du projet

### Problématique

Aujourd'hui, l'ensemble du système de gestion du parking repose sur une architecture 100 % Cloud. La gestion des accès, les paiements et le contrôle des entrées et sorties dépendent donc entièrement de la connexion Internet : la moindre coupure réseau rend les installations inutilisables.

Ce risque s'est concrétisé en mars 2026. Des travaux de voirie ont coupé la connexion Internet pendant 48 heures. Pendant cette période, le système a été totalement indisponible, ce qui a entraîné une perte d'exploitation estimée à 6 000 €.

### Parties prenantes

|Rôle|Personne(s)|
|---|---|
|Client / commanditaire|M. Jean-Luc Bertrand, directeur d'exploitation|
|Prestataires|Maxime Derick, Gregory Kabasele, Liam Bruyère, Vladyslav Volodichev|
|Utilisateurs du système|Agents d'accueil, superviseur(s), clients horaires, abonnés|
|Autres parties concernées|[Fournisseur actuel de la solution Cloud ? Fournisseur des bornes et caisses ? À confirmer]|

### Grandes lignes du projet

Le projet consiste à remplacer la solution actuelle par une application hébergée localement, sur l'infrastructure de la Régie. Les opérations essentielles (accès, paiements aux bornes, contrôle des entrées et sorties) doivent continuer à fonctionner sans connexion Internet. L'application offrira aussi une interface de supervision permettant de suivre l'activité du parking, les paiements et les abonnés.

## 1.3. Objectifs du projet

### Objectifs mesurables

- **O-1 Continuité de service** : pendant une coupure Internet d'au moins 48 heures, 100 % des entrées, sorties et paiements en borne restent possibles, sans intervention humaine. [Durée à confirmer avec le client]
- **O-2 Supervision** : l'agent ou le superviseur peut consulter à tout moment l'occupation du parking, les passages, l'état des paiements et les abonnés depuis une interface unique. [Délai de mise à jour à préciser, ex. : moins de 5 secondes]
- **O-3 Fiabilité des données** : aucune perte ni aucun doublon de données (passages, paiements) lors d'une coupure ou au retour de la connexion.

### Plus-value pour le client

- Suppression des pertes d'exploitation liées aux coupures Internet : environ 6 000 € par incident de 48 heures, soit environ 125 € par heure d'indisponibilité.
- Maintien du service aux clients et aux abonnés, y compris la nuit et le week-end quand aucun agent n'est présent.
- Indépendance vis-à-vis d'un fournisseur Cloud pour les fonctions critiques. [Gain sur l'abonnement Cloud actuel ? À vérifier]

### Risques en cas de non-réalisation

- Nouvelle panne totale à chaque coupure réseau, avec perte de recettes et parking inaccessible.
- Dégradation de l'image de la Régie auprès des clients et surtout des abonnés, qui paient pour un accès garanti.
- Impossibilité de contrôler les entrées et sorties pendant la panne (barrières bloquées ou laissées ouvertes).

### Alternatives possibles

- **Doubler la connexion Internet** (ligne de secours 4G/5G ou second opérateur) : moins coûteux, mais ne protège pas contre une panne du fournisseur Cloud lui-même.
- **Procédure manuelle de secours** (barrières ouvertes et encaissement par l'agent) : impossible en dehors des heures de présence de l'agent (RM-03, RM-04).

# 2. Description générale

## 2.1. Vue d'ensemble du produit et de son environnement

L'application de gestion du parking Valmont est hébergée sur un serveur local, dans les locaux de la Régie. Elle centralise la gestion des accès, des tickets, des paiements et des abonnés, ainsi que la supervision de l'activité. Toutes les fonctions critiques (entrées, sorties, paiements en borne) fonctionnent sans connexion Internet.

### Systèmes existants avec lesquels la solution doit communiquer

|Équipement / système|Rôle|Interface|
|---|---|---|
|Bornes d'entrée|Délivrent les tickets, lisent les badges abonnés|[Protocole / API à identifier]|
|Bornes de sortie|Lisent tickets et badges, autorisent la sortie|[À identifier]|
|Barrières|S'ouvrent sur ordre des bornes|[Pilotées par les bornes ou par le système ? À confirmer]|
|Lecteurs de plaques|Lisent la plaque à chaque passage (D-02)|[À identifier]|
|Caisses automatiques|Encaissent les tickets (espèces, carte, sans contact)|[À identifier]|
|Terminaux de paiement par carte|Autorisation des paiements bancaires|[Fonctionnement hors ligne possible ? À confirmer avec le fournisseur]|
|Panneau d'occupation|Affiche les places libres aux clients (D-05)|[À identifier]|
|Système Cloud actuel|Solution à remplacer|[Données à reprendre ? Voir 2.5]|

## 2.2. Profils utilisateurs (acteurs)

|Acteur|Qui|Attentes vis-à-vis du système|Familiarité informatique|Contraintes|
|---|---|---|---|---|
|Client horaire|Automobiliste de passage|Entrer, payer et sortir rapidement|Variable, souvent faible|Utilise uniquement les bornes et caisses, sans aide la nuit et le week-end|
|Abonné|Client avec abonnement|Entrer et sortir avec son badge sans attente|Variable|Accès garanti 24h/24 (RM-01)|
|Agent d'accueil|Employé de la Régie, présent en semaine (RM-03)|Gérer les abonnés, les tickets perdus, les encaissements et la clôture de caisse|Utilisateur bureautique|Doit pouvoir agir vite face à un client au guichet|
|Superviseur|[M. Bertrand ? Autre responsable ? À confirmer]|Vue d'ensemble de l'activité, des paiements et des anomalies|Bonne|[Consultation depuis l'extérieur du site ? À confirmer]|

## 2.3. Périmètre

### Inclus

- Hébergement de l'application sur une infrastructure locale.
- Gestion des tickets, des passages, des paiements et des abonnés.
- Communication avec les équipements existants listés en 2.1.
- Supervision de l'activité via une interface centralisée.
- Maintien des fonctionnalités critiques en cas de coupure Internet.
- Clôture de caisse par l'agent.

### Exclus

- Hébergement de l'application ou de ses composants sur une infrastructure Cloud.
- [À valider avec le client] Fourniture ou remplacement du matériel (bornes, barrières, caisses, lecteurs).
- [À valider] Application mobile, paiement en ligne et réservation de places.
- [À valider] Gestion de plusieurs sites (voir la question sur « parkings » au pluriel).

## 2.4. Règles métier

- RM-01 : Le parking est ouvert 24h/24, 7j/7.
- RM-02 : Le parking compte 220 places.
- RM-03 : Un agent d'accueil est présent du lundi au vendredi, de 7h00 à 19h00, hors jours fériés.
- RM-04 : En dehors des heures de présence de l'agent (soirs, week-ends, jours fériés), le parking fonctionne de manière entièrement automatisée.
- RM-05 : Tarification horaire : [grille tarifaire à obtenir auprès du client].
- RM-06 : Un ticket perdu est facturé [forfait de X € / tarif depuis l'heure d'entrée lue par la plaque ? À confirmer].
- RM-07 : Après paiement, le client dispose de [X minutes] pour sortir.
- RM-08 : Un abonné ne peut entrer que si son abonnement est valide et son badge actif.

## 2.5. Données

| Code | Donnée            | Contenu                                                                                                        | Origine                                       | Volume                             | Conservation / confidentialité                                                  | Opérations (acteur, fonctionnalité)                                                                                                                                            |
| ---- | ----------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| D-01 | Ticket            | N° de ticket (unique), date et heure d'entrée, plaque, statut (en cours, payé, perdu)                          | Borne d'entrée                                | [X par jour]                       | [Durée à définir] ; contient une plaque (donnée personnelle)                    | Créer : borne d'entrée (F-01) ; Consulter : agent, borne de sortie, caisse auto (F-02 à F-05) ; Marquer payé : caisse auto, agent (F-03, F-05) ; Déclarer perdu : agent (F-04) |
| D-02 | Passage           | Date et heure, sens (entrée/sortie), plaque lue, ticket (D-01) ou badge (D-04), borne                          | Bornes d'entrée et de sortie                  | [~2 par ticket ou trajet d'abonné] | [Durée à définir], puis anonymisation de la plaque (RGPD)                       | Enregistrer : bornes (F-01, F-02) ; Consulter : agent pour ticket perdu, superviseur (F-04, F-07) ; jamais modifié                                                             |
| D-03 | Paiement          | Montant, mode (espèces, carte, sans contact), date et heure, ticket (D-01), lieu d'encaissement                | Caisse auto, agent                            | [X par jour]                       | [Durée légale comptable à vérifier] ; aucune donnée de carte bancaire conservée | Enregistrer : caisse auto, agent (F-03, F-05) ; Consulter : agent, superviseur (F-07, F-08) ; Annuler : agent avec justification (F-05)                                        |
| D-04 | Abonné            | Nom, coordonnées, plaque(s), type et dates d'abonnement, n° de badge (unique), statut du badge (actif, bloqué) | [Reprise du système Cloud ?], puis agent      | [Nombre d'abonnés ?]               | [Durée après fin d'abonnement], puis anonymisation ; donnée personnelle         | Inscrire, modifier, renouveler, bloquer/débloquer le badge, mettre fin : agent (F-06) ; Consulter : agent, bornes pour vérifier le badge (F-01, F-02, F-06)                    |
| D-05 | Occupation        | Capacité totale (RM-02), places occupées, places restantes                                                     | Calculée par le système à partir des passages | Temps réel                         | [Historique à garder ?]                                                         | Mettre à jour : système (F-01, F-02) ; Consulter : clients via panneau, agent, superviseur (F-07) ; Corriger : agent (F-07)                                                    |
| D-06 | Clôture de caisse | Date, agent, total théorique par mode de paiement, montant compté, écart                                       | Agent                                         | [1 par jour ouvrable ?]            | [Durée légale comptable à vérifier]                                             | Créer, valider : agent (F-08) ; Consulter : agent, superviseur (F-07, F-08) ; non modifiable une fois validée                                                                  |


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


