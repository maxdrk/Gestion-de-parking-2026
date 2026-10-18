# 3. Exigences

###### _Cette partie reprend le template de référence du cours. L'IA Claude Opus 5.5, en effort « Moyen », a été utilisée pour clarifier la formulation, vérifier certaines pistes de rédaction avancée par l’auteur et relire la cohérence du document. Le contenu a été vérifié et validé par l'auteur._
## 3.1. Exigences fonctionnelles

### Vue d'ensemble

| ID | Fonctionnalité | Acteur(s) | Priorité |
| --- | --- | --- | --- |
| F-01 | Entrer dans le parking | Client horaire, abonné | Indispensable |
| F-02 | Sortir du parking | Client horaire, abonné | Indispensable |
| F-03 | Payer à la caisse automatique | Client horaire | Indispensable |
| F-04 | Gérer un ticket perdu | Agent | Souhaitable |
| F-05 | Encaisser au guichet | Agent | Indispensable |
| F-06 | Gérer les abonnés | Agent | Indispensable |
| F-07 | Superviser le parking | Agent, directeur | Indispensable |
| F-08 | Clôturer la caisse | Agent | Indispensable |
| F-09 | Tracer les incidents | Agent, directeur | Indispensable |

### Minimum Viable Product

**Périmètre du MVP : F-01, F-02 et F-03**, avec le journal non modifiable (ENF-02) et la reprise après panne (ENF-03, ENF-04).

**Justification** : M. Bertrand l'a dit clairement, la priorité absolue est que les entrées et les sorties fonctionnent sans accroc, même sans Internet ; le reste peut attendre. Le paiement à la caisse (F-03) est inclus, car un client horaire ne peut pas sortir sans avoir payé. Ce MVP permet de vérifier rapidement le point central du projet : un parking qui fonctionne entièrement en local.

### F-01 - Entrer dans le parking

**Acteur(s) :** client horaire, abonné
**Priorité :** indispensable

#### Description

Le client horaire prend un ticket à la borne d'entrée. L'abonné présente son badge. La caméra lit la plaque du véhicule, puis la barrière s'ouvre.

#### Exigences

- EF-01.1 La borne d'entrée délivre un ticket (D-01) portant un numéro unique, la date et l'heure d'entrée.
- EF-01.2 À chaque entrée, le système enregistre un passage (D-02) avec la plaque lue, l'heure, et le ticket ou le badge.
- EF-01.3 Un abonné dont le badge est valide entre sans prendre de ticket (RM-08).
- EF-01.4 Un badge expiré ou désactivé est refusé, et la borne invite l'abonné à prendre un ticket (RM-08).
- EF-01.5 Le panneau affiche « COMPLET » dès que les 190 places publiques sont occupées (RM-07). Comportement de la borne d'entrée dans ce cas : voir Q-08.
- EF-01.6 Un abonné dont le badge est valide peut entrer même quand le panneau affiche « COMPLET » (RM-07, voir Q-09).
- EF-01.7 Chaque entrée met à jour l'occupation (D-05).

#### Critères d'acceptation

- EF-01.1 Un client se présente à 14h03 : il reçoit un ticket indiquant 14h03, dont le numéro n'a jamais été attribué.
- EF-01.2 Le véhicule 1-ABC-123 entre avec un ticket : le passage enregistré contient la plaque 1-ABC-123, l'heure et le numéro du ticket.
- EF-01.3 Un abonné « permanent » dont l'abonnement est valide présente son badge : la barrière s'ouvre, aucun ticket n'est délivré.
- EF-01.4 Un abonné dont l'abonnement a pris fin la veille présente son badge : l'entrée par badge est refusée, la borne lui propose un ticket.
- EF-01.5 189 places publiques sont occupées et le panneau indique 1 place libre. Un client entre : le panneau affiche « COMPLET ».
- EF-01.6 Les 190 places publiques sont occupées : un abonné avec un badge valide entre normalement.
- EF-01.7 Après l'entrée d'un client horaire, le nombre de places publiques occupées augmente de 1 dans la supervision.

#### Données impliquées

Crée D-01 et D-02 ; consulte D-04 (validité du badge) ; met à jour D-05.

### F-02 - Sortir du parking

**Acteur(s) :** client horaire, abonné
**Priorité :** indispensable

#### Description

Le client horaire présente son ticket payé à la borne de sortie. L'abonné présente son badge. Si la sortie est autorisée, la barrière s'ouvre.

#### Exigences

- EF-02.1 La borne de sortie accepte un ticket payé, si le client sort dans les 15 minutes qui suivent le paiement (RM-06, voir Q-21).
- EF-02.2 Au-delà de ce délai, la borne refuse le ticket et indique au client qu'il doit payer un complément (RM-06, voir Q-04).
- EF-02.3 Un ticket non payé est refusé.
- EF-02.4 Un ticket déjà utilisé pour sortir est refusé.
- EF-02.5 Un abonné dont le badge est valide sort en présentant son badge (RM-08).
- EF-02.6 Chaque sortie enregistre un passage (D-02) et met à jour l'occupation (D-05).

#### Critères d'acceptation

- EF-02.1 Un client paie à 14h00 et se présente à la sortie à 14h10 : la barrière s'ouvre.
- EF-02.2 Un client paie à 14h00 et se présente à la sortie à 14h20 : le ticket est refusé, et un complément de 0,60 € lui est indiqué (2 quarts d'heure entamés depuis 14h00, sans gratuité).
- EF-02.3 Un client présente un ticket non payé : le ticket est refusé, avec un message l'invitant à payer à la caisse.
- EF-02.4 Après une sortie, le même ticket est présenté à nouveau : il est refusé.
- EF-02.5 Un abonné avec un badge valide présente son badge : la barrière s'ouvre.
- EF-02.6 Après la sortie d'un client horaire, le nombre de places publiques occupées diminue de 1 dans la supervision.

#### Données impliquées

Consulte D-01, D-03 et D-04 ; met à jour le statut de D-01 (« sorti ») ; crée D-02 ; met à jour D-05.


### F-03 - Payer à la caisse automatique

**Acteur(s) :** client horaire
**Priorité :** indispensable

#### Description

Le client insère son ticket dans la caisse automatique, qui affiche le montant à payer. Il paie en espèces, par carte ou sans contact. Le paiement est simulé : aucun paiement bancaire réel n'est effectué.

#### Exigences

- EF-03.1 La caisse affiche le montant calculé selon le tarif (RM-05), à partir de l'heure d'entrée du ticket.
- EF-03.2 Un stationnement de 30 minutes ou moins est gratuit (RM-05).
- EF-03.3 Entre 7h00 et 19h00, chaque quart d'heure entamé au-delà des 30 minutes gratuites coûte 0,30 € (RM-05).
- EF-03.4 Entre 19h00 et 7h00, le forfait de nuit de 3 € s'applique (RM-05, voir Q-01 et Q-02).
- EF-03.5 Le montant ne dépasse pas 12 € par période de 24 heures depuis l'entrée (RM-05, voir Q-03).
- EF-03.6 Le client peut payer en espèces, par carte ou sans contact (paiement simulé).
- EF-03.7 Après le paiement, le ticket passe au statut « payé », et le paiement (D-03) est enregistré avec son heure.
- EF-03.8 La caisse calcule le complément d'un ticket dont le délai de sortie est dépassé (RM-06, voir Q-04).

#### Critères d'acceptation

- EF-03.1 Ticket entré à 10h00, inséré à 11h00 : la caisse affiche 0,60 € (30 minutes payantes, soit 2 quarts d'heure).
- EF-03.2 Ticket entré à 10h00, inséré à 10h30 : la caisse affiche 0,00 €. Inséré à 10h31 : elle affiche 0,30 €.
- EF-03.3 Ticket entré à 10h00, inséré à 10h40 : la caisse affiche 0,30 € (10 minutes payantes, 1 quart d'heure entamé). Ce cas a été confirmé par M. Bertrand.
- EF-03.4 Ticket entré à 20h00, inséré à 6h00 le lendemain : la caisse affiche 3,00 €.
- EF-03.5 Ticket entré à 7h00, inséré à 19h00 : le calcul donne 13,80 €, la caisse affiche 12,00 €.
- EF-03.6 Le client paie par carte : le paiement est enregistré avec le mode « carte ».
- EF-03.7 Après le paiement, le ticket apparaît comme « payé » dans la supervision, avec l'heure du paiement.
- EF-03.8 Ticket payé à 14h00, inséré à nouveau à 14h20 : la caisse affiche un complément de 0,60 €.

#### Données impliquées

Consulte D-01 ; met à jour le statut de D-01 ; crée D-03.

### F-04 - Gérer un ticket perdu

**Acteur(s) :** agent
**Priorité :** souhaitable

#### Description

Un client a perdu son ticket. L'agent retrouve son heure d'entrée à partir de la plaque, déclare le ticket perdu et encaisse le montant dû. Le tarif d'un ticket perdu et la procédure de nuit ne sont pas encore connus (Q-11).

#### Exigences

- EF-04.1 L'agent recherche un véhicule présent à partir de sa plaque, et retrouve son ticket et son heure d'entrée (D-02).
- EF-04.2 L'agent déclare le ticket perdu : son statut passe à « perdu » (D-01).
- EF-04.3 Le montant appliqué à un ticket perdu respecte la règle à définir (Q-11).

#### Critères d'acceptation

- EF-04.1 Le véhicule 1-ABC-123 est entré à 9h12 : l'agent saisit la plaque et retrouve le ticket entré à 9h12.

#### Données impliquées

Consulte D-02 ; met à jour D-01 ; crée D-03.
### F-05 - Encaisser au guichet

**Acteur(s) :** agent
**Priorité :** indispensable

#### Description

L'agent encaisse les clients qui se présentent au guichet. Quand la caisse automatique est en panne pendant ses heures de présence, il passe en mode dégradé : il note chaque paiement à la main avec l'heure réelle, puis l'encode dans le système après la reprise.

#### Exigences

- EF-05.1 L'agent encaisse un ticket au guichet, avec le même calcul qu'à la caisse automatique (RM-05, RM-06).
- EF-05.2 L'agent encode a posteriori un paiement noté à la main, en indiquant son heure réelle.
- EF-05.3 Un paiement encodé a posteriori est identifié comme tel dans la liste des paiements (D-03).
- EF-05.4 L'agent annule un paiement en indiquant obligatoirement une justification.
- EF-05.5 Un paiement annulé reste visible dans la liste des paiements, avec sa justification.

Sortie des clients qui ont payé à la main pendant la panne : voir Q-07.

#### Critères d'acceptation

- EF-05.1 Un ticket entré à 10h00 est encaissé au guichet à 10h40 : le montant affiché est 0,30 €, comme à la caisse automatique.
- EF-05.2 La caisse est en panne de 10h00 à 11h00. À 11h05, l'agent encode un paiement de 1,20 € noté à 10h20 : le paiement est enregistré avec l'heure 10h20.
- EF-05.3 Dans la liste des paiements, le paiement de 10h20 porte la mention « encodé a posteriori ».
- EF-05.4 L'agent tente d'annuler un paiement sans justification : l'annulation est refusée.
- EF-05.5 Après l'annulation, le paiement apparaît comme « annulé », avec la justification saisie.

#### Données impliquées

Consulte D-01 ; crée et annule des D-03 ; met à jour le statut de D-01.

### F-06 - Gérer les abonnés

**Acteur(s) :** agent
**Priorité :** indispensable

#### Description

L'agent inscrit les abonnés au guichet, renouvelle leurs abonnements et remplace les badges perdus. Pour un renouvellement, il vérifie l'identité et le paiement de l'abonné. En cas de perte, il délivre un nouveau badge après vérification, et l'ancien est désactivé immédiatement.

#### Exigences

- EF-06.1 L'agent inscrit un abonné (D-04) avec une formule « jour » ou « permanent », et lui attribue un badge (RM-08, voir Q-10).
- EF-06.2 L'agent modifie les coordonnées et les plaques d'un abonné.
- EF-06.3 L'agent renouvelle un abonnement : la date de fin est prolongée.
- EF-06.4 L'agent remplace un badge perdu : un nouveau badge est attribué, et l'ancien est désactivé immédiatement.
- EF-06.5 L'agent met fin à un abonnement : le badge est désactivé.
- EF-06.6 L'agent consulte la liste des abonnés, avec leur formule et leur date de fin d'abonnement.

#### Critères d'acceptation

- EF-06.1 L'agent inscrit un abonné « permanent » : son badge permet d'entrer immédiatement (EF-01.3).
- EF-06.2 Après l'ajout d'une seconde plaque, la fiche de l'abonné affiche les deux plaques.
- EF-06.3 Un abonnement qui se termine le 31/10 est renouvelé : le badge reste accepté le 01/11.
- EF-06.4 Juste après le remplacement, l'ancien badge est refusé à l'entrée et le nouveau est accepté.
- EF-06.5 Après la fin d'un abonnement, le badge est refusé à l'entrée.
- EF-06.6 La liste affiche chaque abonné avec sa formule et sa date de fin.

#### Données impliquées

Crée, consulte et modifie des D-04.

### F-07 - Superviser le parking

**Acteur(s) :** agent, directeur
**Priorité :** indispensable

#### Description

Le directeur et les agents suivent l'activité du parking depuis le guichet : occupation, passages, paiements, véhicules présents et incidents. La supervision se fait sur place (supervision à distance : voir Q-17).

#### Exigences

- EF-07.1 La supervision affiche le nombre de places occupées et libres, séparément pour les places publiques et les places abonnés (RM-02, D-05).
- EF-07.2 La supervision affiche les passages d'une journée choisie, avec l'heure, le sens, la plaque, et le ticket ou le badge (D-02).
- EF-07.3 La supervision affiche les paiements d'une journée choisie, avec le montant, le mode et le lieu d'encaissement (D-03).
- EF-07.4 La supervision affiche la liste des véhicules présents dans le parking.
- EF-07.5 La supervision affiche les incidents non résolus (D-07).
- EF-07.6 L'agent peut corriger le nombre de places occupées, en indiquant une justification (D-05).

Délai de mise à jour de l'affichage : voir Q-15.

#### Critères d'acceptation

- EF-07.1 Avec 150 clients horaires et 20 abonnés présents, la supervision affiche 40 places publiques libres et 10 places abonnés libres.
- EF-07.2 Pour le 15/10, la supervision affiche tous les passages de cette journée, et uniquement ceux-là.
- EF-07.3 Pour le 15/10, la supervision affiche tous les paiements de cette journée, avec leur mode et leur lieu.
- EF-07.4 Un véhicule entré à 9h00 et pas encore sorti apparaît dans la liste ; un véhicule sorti n'y apparaît plus.
- EF-07.5 Un incident ouvert apparaît ; après sa résolution (EF-09.3), il disparaît de la liste des incidents non résolus.
- EF-07.6 Une correction sans justification est refusée.

#### Données impliquées

Consulte D-01, D-02, D-03, D-04, D-05 et D-07 ; corrige D-05.

### F-08 - Clôturer la caisse

**Acteur(s) :** agent
**Priorité :** indispensable

#### Description

Chaque soir, l'agent clôture la caisse : le système calcule le total théorique par mode de paiement, l'agent saisit le montant réellement compté, et le système calcule l'écart. Clôture du week-end et procédure en cas d'écart : voir Q-12.

#### Exigences

- EF-08.1 Le système calcule le total théorique de la journée pour chaque mode de paiement (D-03).
- EF-08.2 L'agent saisit le montant compté.
- EF-08.3 Le système calcule et affiche l'écart entre le total théorique et le montant compté.
- EF-08.4 Une clôture validée ne peut plus être modifiée (D-06).
- EF-08.5 Un écart différent de zéro crée un incident (F-09).

#### Critères d'acceptation

- EF-08.1 Pour une journée avec 3 paiements en espèces de 1,20 €, 0,60 € et 3,00 €, le total théorique en espèces est de 4,80 €.
- EF-08.2 L'agent saisit 4,80 € : le montant est enregistré dans la clôture.
- EF-08.3 Total théorique en espèces de 4,80 €, montant compté de 4,50 € : l'écart affiché est de -0,30 €.
- EF-08.4 Après validation, toute tentative de modifier la clôture est refusée.
- EF-08.5 L'écart de -0,30 € apparaît comme incident dans la supervision (EF-07.5).

#### Données impliquées

Consulte D-03 ; crée D-06 ; crée D-07 en cas d'écart.

### F-09 - Tracer les incidents

**Acteur(s) :** agent, directeur
**Priorité :** indispensable

#### Description

M. Bertrand veut être informé de tout événement qui empêche un client d'entrer, de payer ou de sortir normalement. Pour chaque incident, il veut savoir ce qui s'est passé, à quelle heure, et ce qui a été fait pour le résoudre. Information du directeur en dehors de ses heures de présence : voir Q-16.

#### Exigences

- EF-09.1 Le système enregistre un incident (D-07) dans chacun des cas suivants :
  - une barrière ne se lève pas ;
  - une borne refuse un paiement ;
  - un ticket est illisible ;
  - un badge ne fonctionne pas ;
  - un écart de caisse est constaté (EF-08.5) ;
  - le panneau d'affichage tombe en panne ;
  - la caisse automatique tombe en panne.
- EF-09.2 Chaque incident indique la date, l'heure, l'équipement concerné et une description.
- EF-09.3 L'agent indique l'action réalisée et marque l'incident comme résolu.
- EF-09.4 Le directeur consulte l'historique des incidents, résolus ou non.
- EF-09.5 Un incident ne peut pas être supprimé.

Panne de la caisse la nuit ou le week-end, sans agent : voir Q-06.

#### Critères d'acceptation

- EF-09.1 On simule une barrière de sortie qui ne se lève pas à 22h14 : un incident apparaît dans la supervision.
- EF-09.2 L'incident affiche la date, 22h14, « barrière de sortie » et la description du problème.
- EF-09.3 Le lendemain, l'agent saisit « barrière redémarrée » et résout l'incident : il apparaît comme résolu, avec l'action réalisée.
- EF-09.4 Le directeur voit l'incident du 22h14 dans l'historique, avec l'action réalisée.
- EF-09.5 Aucune action ne permet de supprimer un incident.

#### Données impliquées

Crée, consulte et met à jour D-07.
## 3.2. Exigences non fonctionnelles

| ID | Exigence | Vérification |
| --- | --- | --- |
| ENF-01 | **Autonomie** : le système assure les entrées, les sorties et les paiements en permanence, 24h/24 et 7j/7, sans aucune connexion Internet. | Exécution des critères d'acceptation de F-01, F-02 et F-03 avec le serveur déconnecté d'Internet. |
| ENF-02 | **Journal** : chaque entrée, paiement et sortie est inscrit dans un journal au moment où il a lieu. Aucune ligne du journal ne peut être modifiée ni supprimée. | Tentative de modification et de suppression d'une ligne, avec un compte agent et avec le compte du directeur : refusée dans tous les cas. |
| ENF-03 | **Aucune perte de données** : après un arrêt brutal du serveur, tous les passages et paiements enregistrés avant l'arrêt sont présents. | Coupure brutale du serveur pendant une série de 50 passages simulés ; comparaison du journal avec la liste des passages effectués. |
| ENF-04 | **Redémarrage** : après une panne, le système redémarre en moins d'une minute et connaît exactement les véhicules présents et les tickets payés. | Chronométrage de 10 redémarrages ; comparaison des véhicules présents avant et après chaque redémarrage. |
| ENF-05 | **Autonomie des utilisateurs** : après la formation (L-03), le directeur et chaque agent réalisent seuls un encaissement au guichet, l'encodage d'un paiement en mode dégradé, le renouvellement d'un abonnement et une clôture de caisse. | Test avec M. Bertrand et les 2 agents, lors de la recette. |
| ENF-06 | **Données personnelles** : aucune donnée personnelle n'est collectée en dehors de celles listées en 2.5, et les durées de conservation (Q-13) sont respectées. | Revue des écrans de saisie ; vérification de la suppression ou de l'anonymisation des données arrivées à échéance. |

# 4. Contraintes

- **Fonctionnement local** : le système fonctionne sur place, sans aucune dépendance à Internet (ENF-01). C'est la leçon de la coupure de mars 2026.
- **Matériel simulé** : le projet simule les équipements du site : borne d'entrée, borne de sortie, caisse automatique, guichet de l'agent, caméra de lecture des plaques à l'entrée, barrières, panneau d'affichage des places libres et badges des abonnés.
- **Hors projet** (confirmé par M. Bertrand) : le paiement bancaire réel et le pilotage physique des barrières. À ajouter aussi aux exclusions du périmètre (2.3).
- **Réglementation** :
  - le tarif est fixé par une délibération communale (décembre 2024) ;
  - le traitement des plaques et des données des abonnés respecte le RGPD ;
  - le réviseur communal contrôle les comptes et le journal une fois par an, sur place. Ils doivent donc rester consultables localement.
- **Technologie** : aucune technologie imposée connue à ce jour (Q-19).
- **Délais** : cahier des charges remis le 12/10, diagrammes UML le 19/10, démo du MVP sur GitHub le 02/11, démo client et mise en production le 07/12.

# 5. Budget

Le développement est réalisé dans le cadre d'un projet étudiant.

Charge estimée : 4 étudiants × 30 heures = 120 heures de travail. [
# 6. Livrables et planning

## 6.1. Livrables

- **L-01** L'application, installée sur le serveur local, avec la simulation des équipements du site.
- **L-02** Une procédure pratique pour le directeur et les agents : courte et rapide à consulter, couvrant l'utilisation courante et les cas de panne (caisse en panne, mode dégradé).
- **L-03** La formation du directeur et des 2 agents : guichet, caisse, bornes, supervision et mode dégradé. Le contenu est proposé au client, qui le valide.
- **L-04** Le code source et sa documentation technique.

## 6.2. Échéances

| Semaine | Date          | Échéance                                                                                                                           |
| ------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| S5      | 12/10         | Remise du cahier des charges, validation par M. Bertrand                                                                           |
| S6      | 19/10         | Conception : diagrammes UML                                                                                                        |
| —       | 26/10         | Congé de Toussaint                                                                                                                 |
| S7      | 02/11         | Démo du MVP sur GitHub : F-01, F-02 et F-03 (entrées, sorties, paiement à la caisse)                                               |
| S8      | 09/11         | Spécifications détaillées                                                                                                          |
| S8 – S9 | 09/11 – 16/11 | Développement du second incrément : F-05, F-06, F-07, F-08 et F-09                                                                 |
| S10     | 23/11         | Démo du second incrément                                                                                                           |
| S11     | 30/11         | Tests : vérification des critères d'acceptation et des exigences non fonctionnelles                                                |
| S12     | 07/12         | Version finale (F-04 si le temps le permet), démo client, formation (L-03), procédure (L-02), mise en production et recette finale |
## 6.3. Retours vers le client

M. Bertrand souhaite être informé régulièrement et valider lui-même que le système répond à ses besoins.

Proposition, à valider avec lui :
- une démo à chaque livraison : MVP le 02/11, second incrément le 23/11, version finale le 07/12 ;
- un point d'avancement de 15 minutes toutes les deux semaines, pour répondre aux questions ouvertes ;
- validation de chaque livraison par M. Bertrand, sur base des critères d'acceptation de la section 3.1.


# Questions ouvertes 

| ID | Question | Éléments impactés |
| --- | --- | --- |
| Q-01 | Le forfait de nuit de 3 € s'applique-t-il une fois par nuit, ou une fois par stationnement ? | RM-05, EF-03.4 |
| Q-02 | Comment calcule-t-on un stationnement à cheval sur le jour et la nuit (ex : entrée à 18h30, sortie à 20h00) ? | RM-05, EF-03 |
| Q-03 | Au-delà de 24 heures, le maximum de 12 € s'applique-t-il à nouveau pour chaque période de 24 heures ? | RM-05, EF-03.5 |
| Q-04 | Où se paie le complément après dépassement des 15 minutes, et compte-t-il dans le maximum de 12 € ? | RM-06, EF-02.2, EF-03.8 |
| Q-05 | Les bornes et la caisse rendent-elles la monnaie ? | F-03 |
| Q-06 | Que se passe-t-il si la caisse tombe en panne la nuit ou le week-end, sans agent ? (Piste évoquée : payer à la borne de sortie.) | F-02, F-03, F-09 |
| Q-07 | Pendant une panne de caisse en journée, comment sortent les clients qui ont payé à la main ? | F-05, F-02 |
| Q-08 | Quand les 190 places publiques sont occupées, la borne d'entrée refuse-t-elle de délivrer un ticket ? | EF-01.5 |
| Q-09 | Que se passe-t-il quand les 30 places abonnés sont toutes occupées ? | RM-07, EF-01.6 |
| Q-10 | Quelles sont les heures de la formule « jour », les prix des formules, et le nombre d'abonnés ? | RM-08, F-06, D-04 |
| Q-11 | Combien coûte un ticket perdu, et comment cela se passe-t-il la nuit, sans agent ? | F-04 |
| Q-12 | La clôture de caisse se fait-elle aussi le week-end ? Que fait-on en cas d'écart ? | F-08 |
| Q-13 | Combien de temps conserve-t-on les plaques et les données des abonnés ? | D-02, D-04, ENF-06 |
| Q-14 | Dans quelles langues les bornes doivent-elles s'afficher ? | F-01, F-02, F-03, ENF |
| Q-15 | En combien de temps la supervision doit-elle être mise à jour ? | F-07, ENF |
| Q-16 | Comment le directeur doit-il être informé d'un incident survenu hors des heures de présence ? | F-09 |
| Q-17 | Une supervision à distance est-elle nécessaire, sachant que le système ne doit pas dépendre d'Internet ? | F-07, périmètre (2.3) |
| Q-18 | La plaque est-elle aussi lue à la sortie, ou uniquement à l'entrée ? | D-02, EF-02.6 |
| Q-19 | Une technologie est-elle imposée ? Le serveur local est-il fourni par la Régie ? | 4, 5 |
| Q-20 | Pour quand la mise en service est-elle souhaitée, et comment passer de l'ancien système au nouveau sans fermer le parking ? | 6.2 |
| Q-21 | Un client qui se présente à la sortie exactement 15 minutes après son paiement peut-il sortir ? | RM-06, EF-02.1 |
