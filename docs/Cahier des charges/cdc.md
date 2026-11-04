# Cahier des charges - Gestion de parkings Valmont


>  L’intelligence artificielle **Claude Opus 5.5**, utilisée avec un niveau d’effort « Moyen », a été mobilisée pour les parties 3 à 6 afin de clarifier certaines formulations, d’examiner des pistes de rédaction avancées par l’auteur et de vérifier la cohérence globale du document. **ChatGPT 6**, également utilisé avec un niveau d’effort « Moyen », a été employé pour les parties 1 à 3 dans un objectif similaire. L’ensemble du contenu généré ou reformulé à l’aide de ces outils a été relu, vérifié et validé par l’auteur, qui en assume la responsabilité finale.


**Version :** V1

**Date :** 18/10/2026

**Auteurs :**

1. Maxime Derick
2. Gregory Kabasele
3. Liam Bruyère
4. Vladyslav Volodichev

**Statut :** Document de travail - à valider avec le client.

## Conventions d'identification

| Élément | Format | Exemple |
| --- | --- | --- |
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

| Rôle | Personne(s) |
| --- | --- |
| Client / commanditaire | M. Jean-Luc Bertrand, directeur d'exploitation |
| Prestataires | Maxime Derick, Gregory Kabasele, Liam Bruyère, Vladyslav Volodichev |
| Utilisateurs du système | Agents d'accueil, superviseur(s), clients horaires, abonnés |
| Autres parties concernées | [Fournisseur actuel de la solution Cloud ? Fournisseur des bornes et caisses ? À confirmer] |

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

| Équipement / système | Rôle | Interface |
| --- | --- | --- |
| Bornes d'entrée | Délivrent les tickets, lisent les badges abonnés | [Protocole / API à identifier] |
| Bornes de sortie | Lisent tickets et badges, autorisent la sortie | [À identifier] |
| Barrières | S'ouvrent sur ordre des bornes | [Pilotées par les bornes ou par le système ? À confirmer] |
| Lecteurs de plaques | Lisent la plaque à chaque passage (D-02) | [À identifier] |
| Caisses automatiques | Encaissent les tickets (espèces, carte, sans contact) | [À identifier] |
| Terminaux de paiement par carte | Autorisation des paiements bancaires | [Fonctionnement hors ligne possible ? À confirmer avec le fournisseur] |
| Panneau d'occupation | Affiche les places libres aux clients (D-05) | [À identifier] |
| Système Cloud actuel | Solution à remplacer | [Données à reprendre ? Voir 2.5] |

## 2.2. Profils utilisateurs (acteurs)

| Acteur | Qui | Attentes vis-à-vis du système | Familiarité informatique | Contraintes |
| --- | --- | --- | --- | --- |
| Client horaire | Automobiliste de passage | Entrer, payer et sortir rapidement | Variable, souvent faible | Utilise uniquement les bornes et caisses, sans aide la nuit et le week-end |
| Abonné | Client avec abonnement | Entrer et sortir avec son badge sans attente | Variable | Accès garanti 24h/24 (RM-01) |
| Agent d'accueil | Employé de la Régie, présent en semaine (RM-03) | Gérer les abonnés, les tickets perdus, les encaissements et la clôture de caisse | Utilisateur bureautique | Doit pouvoir agir vite face à un client au guichet |
| Superviseur | [M. Bertrand ? Autre responsable ? À confirmer] | Vue d'ensemble de l'activité, des paiements et des anomalies | Bonne | [Consultation depuis l'extérieur du site ? À confirmer] |

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


| Référence | Règle métier |
|---|---|
| **RM-01** | Le parking est accessible 24 h/24 et 7 j/7. |
| **RM-02** | Le parking dispose d'une capacité totale de 220 places. |
| **RM-03** | Un agent d'accueil est présent du lundi au vendredi, de 7 h à 19 h, hors jours fériés. |
| **RM-04** | En dehors des heures de présence de l'agent d'accueil (soirées, week-ends et jours fériés), le parking fonctionne de manière entièrement automatisée. |
| **RM-05** | Les trente premières minutes de stationnement sont gratuites. |
| **RM-06** | De 7 h à 19 h, chaque quart d'heure entamé est facturé 0,30 €. |
| **RM-07** | De 19 h à 7 h, un forfait de nuit de 3 € est appliqué. |
| **RM-08** | Le montant total facturé est plafonné à 12 € par période de 24 heures, calculée à partir de l'heure d'entrée du véhicule. |
| **RM-09** | En cas de perte de ticket, un forfait de 25 € est appliqué, sauf si l'agent retrouve l'heure d'entrée du véhicule grâce à la plaque d'immatriculation enregistrée par la caméra d'entrée. Dans ce cas, le tarif normal est appliqué. |
| **RM-10** | Après le paiement, le client dispose de 15 minutes pour quitter le parking. |
| **RM-11** | Au-delà du délai de sortie de 15 minutes, la borne refuse l'ouverture de la barrière. Le client doit alors régler un supplément calculé à partir de l'heure du paiement, sans bénéficier des 30 minutes gratuites. |
| **RM-12** | Un abonné ne peut accéder au parking que si son abonnement est valide et que son badge est actif. |
| **RM-13** | L'abonnement « jour » coûte 60 € par mois et autorise l'accès du lundi au vendredi, de 7 h à 19 h. |
| **RM-14** | L'abonnement « permanent » coûte 100 € par mois et autorise l'accès 24 h/24, 7 j/7, sans limite de durée de stationnement. |
| **RM-15** | Pour un abonnement « jour », toute période de stationnement située en dehors des plages horaires autorisées est facturée au tarif normal applicable. |
| **RM-16** | Un badge expiré ou invalide est refusé. Le client doit alors utiliser un ticket classique pour accéder au parking. |

## 2.5. Données

| Code | Donnée | Contenu | Origine | Volume | Conservation / confidentialité | Opérations (acteur, fonctionnalité) |
| --- | --- | --- | --- | --- | --- | --- |
| D-01 | Ticket | N° de ticket (unique), date et heure d'entrée, plaque, statut (en cours, payé, perdu) | Borne d'entrée | [X par jour] | [Durée à définir] ; contient une plaque (donnée personnelle) | Créer : borne d'entrée (F-01) ; Consulter : agent, borne de sortie, caisse auto (F-02 à F-05) ; Marquer payé : caisse auto, agent (F-03, F-05) ; Déclarer perdu : agent (F-04) |
| D-02 | Passage | Date et heure, sens (entrée/sortie), plaque lue, ticket (D-01) ou badge (D-04), borne | Bornes d'entrée et de sortie | [~2 par ticket ou trajet d'abonné] | [Durée à définir], puis anonymisation de la plaque (RGPD) | Enregistrer : bornes (F-01, F-02) ; Consulter : agent pour ticket perdu, superviseur (F-04, F-07) ; jamais modifié |
| D-03 | Paiement | Montant, mode (espèces, carte, sans contact), date et heure, ticket (D-01), lieu d'encaissement | Caisse auto, agent | [X par jour] | [Durée légale comptable à vérifier] ; aucune donnée de carte bancaire conservée | Enregistrer : caisse auto, agent (F-03, F-05) ; Consulter : agent, superviseur (F-07, F-08) ; Annuler : agent avec justification (F-05) |
| D-04 | Abonné | Nom, coordonnées, plaque(s), type et dates d'abonnement, n° de badge (unique), statut du badge (actif, bloqué) | [Reprise du système Cloud ?], puis agent | [Nombre d'abonnés ?] | [Durée après fin d'abonnement], puis anonymisation ; donnée personnelle | Inscrire, modifier, renouveler, bloquer/débloquer le badge, mettre fin : agent (F-06) ; Consulter : agent, bornes pour vérifier le badge (F-01, F-02, F-06) |
| D-05 | Occupation | Capacité totale (RM-02), places occupées, places restantes | Calculée par le système à partir des passages | Temps réel | [Historique à garder ?] | Mettre à jour : système (F-01, F-02) ; Consulter : clients via panneau, agent, superviseur (F-07) ; Corriger : agent (F-07) |
| D-06 | Clôture de caisse | Date, agent, total théorique par mode de paiement, montant compté, écart | Agent | [1 par jour ouvrable ?] | [Durée légale comptable à vérifier] | Créer, valider : agent (F-08) ; Consulter : agent, superviseur (F-07, F-08) ; non modifiable une fois validée |

# 3. Exigences

## 3.1. Exigences fonctionnelles

### Vue d'ensemble

| ID | Fonctionnalité | Acteur(s) | Priorité | Responsable de l'exigence |
| --- | --- | --- | --- | --- |
| F-01 | Entrer dans le parking | Client horaire, abonné | Indispensable | Maxime Derick |
| F-02 | Sortir du parking | Client horaire, abonné | Indispensable | Maxime Derick |
| F-03 | Payer à la caisse automatique | Client horaire | Indispensable | Vladyslav Volodichev |
| F-04 | Gérer un ticket perdu | Agent | Souhaitable | Vladyslav Volodichev |
| F-05 | Encaisser au guichet | Agent | Indispensable | Liam Bruyere |
| F-06 | Gérer les abonnés | Agent | Indispensable | Liam Bruyere |
| F-07 | Superviser le parking | Agent, directeur | Indispensable | Gregory Kabasele |
| F-08 | Clôturer la caisse | Agent | Indispensable | Gregory Kabasele |
| F-09 | Tracer les incidents | Agent, directeur | Indispensable | Gregory Kabasele |

### Minimum Viable Product

**Périmètre du MVP : F-01, F-02 et F-03**, avec le journal non modifiable (ENF-02) et la reprise après panne (ENF-03, ENF-04).

**Justification** : M. Bertrand l'a dit clairement, la priorité absolue est que les entrées et les sorties fonctionnent sans accroc, même sans Internet ; le reste peut attendre. Le paiement à la caisse (F-03) est inclus, car un client horaire ne peut pas sortir sans avoir payé. Ce MVP permet de vérifier rapidement le point central du projet : un parking qui fonctionne entièrement en local.

---

### F-01 - Entrer dans le parking

**Acteur(s) :** client horaire, abonné
**Priorité :** indispensable

#### Description

Le client horaire prend un ticket à la borne d'entrée. L'abonné présente son badge. La caméra lit la plaque du véhicule, puis la barrière s'ouvre.

#### Exigences

- **EF-01.1** La borne d'entrée délivre un ticket (D-01) portant un numéro unique, la date et l'heure d'entrée.
- **EF-01.2** À chaque entrée, le système enregistre un passage (D-02) avec la plaque lue, l'heure, et le ticket ou le badge.
- **EF-01.3** Un abonné dont le badge est valide entre sans prendre de ticket (RM-08).
- **EF-01.4** Un badge expiré ou désactivé est refusé, et la borne invite l'abonné à prendre un ticket (RM-08).
- **EF-01.5** Le panneau affiche « COMPLET » dès que les 190 places publiques sont occupées (RM-07). Comportement de la borne d'entrée dans ce cas : voir Q-08.
- **EF-01.6** Un abonné dont le badge est valide peut entrer même quand le panneau affiche « COMPLET » (RM-07, voir Q-09).
- **EF-01.7** Chaque entrée met à jour l'occupation (D-05).

#### Critères d'acceptation

- **EF-01.1** Un client se présente à 14h03 : il reçoit un ticket indiquant 14h03, dont le numéro n'a jamais été attribué.
- **EF-01.2** Le véhicule 1-ABC-123 entre avec un ticket : le passage enregistré contient la plaque 1-ABC-123, l'heure et le numéro du ticket.
- **EF-01.3** Un abonné « permanent » dont l'abonnement est valide présente son badge : la barrière s'ouvre, aucun ticket n'est délivré.
- **EF-01.4** Un abonné dont l'abonnement a pris fin la veille présente son badge : l'entrée par badge est refusée, la borne lui propose un ticket.
- **EF-01.5** 189 places publiques sont occupées et le panneau indique 1 place libre. Un client entre : le panneau affiche « COMPLET ».
- **EF-01.6** Les 190 places publiques sont occupées : un abonné avec un badge valide entre normalement.
- **EF-01.7** Après l'entrée d'un client horaire, le nombre de places publiques occupées augmente de 1 dans la supervision.

#### Données impliquées

Crée D-01 et D-02 ; consulte D-04 (validité du badge) ; met à jour D-05.

---

### F-02 - Sortir du parking

**Acteur(s) :** client horaire, abonné
**Priorité :** indispensable

#### Description

Le client horaire présente son ticket payé à la borne de sortie. L'abonné présente son badge. Si la sortie est autorisée, la barrière s'ouvre.

#### Exigences

- **EF-02.1** La borne de sortie accepte un ticket payé, si le client sort dans les 15 minutes qui suivent le paiement (RM-06, voir Q-21).
- **EF-02.2** Au-delà de ce délai, la borne refuse le ticket et indique au client qu'il doit payer un complément (RM-06, voir Q-04).
- **EF-02.3** Un ticket non payé est refusé.
- **EF-02.4** Un ticket déjà utilisé pour sortir est refusé.
- **EF-02.5** Un abonné dont le badge est valide sort en présentant son badge (RM-08).
- **EF-02.6** Chaque sortie enregistre un passage (D-02) et met à jour l'occupation (D-05).

#### Critères d'acceptation

- **EF-02.1** Un client paie à 14h00 et se présente à la sortie à 14h10 : la barrière s'ouvre.
- **EF-02.2** Un client paie à 14h00 et se présente à la sortie à 14h20 : le ticket est refusé, et un complément de 0,60 € lui est indiqué (2 quarts d'heure entamés depuis 14h00, sans gratuité).
- **EF-02.3** Un client présente un ticket non payé : le ticket est refusé, avec un message l'invitant à payer à la caisse.
- **EF-02.4** Après une sortie, le même ticket est présenté à nouveau : il est refusé.
- **EF-02.5** Un abonné avec un badge valide présente son badge : la barrière s'ouvre.
- **EF-02.6** Après la sortie d'un client horaire, le nombre de places publiques occupées diminue de 1 dans la supervision.

#### Données impliquées

Consulte D-01, D-03 et D-04 ; met à jour le statut de D-01 (« sorti ») ; crée D-02 ; met à jour D-05.

---

### F-03 - Payer à la caisse automatique

**Acteur(s) :** client horaire
**Priorité :** indispensable

#### Description

Le client insère son ticket dans la caisse automatique, qui affiche le montant à payer. Il paie en espèces, par carte ou sans contact. Le paiement est simulé : aucun paiement bancaire réel n'est effectué.

#### Exigences

- **EF-03.1** La caisse affiche le montant calculé selon le tarif (RM-05), à partir de l'heure d'entrée du ticket.
- **EF-03.2** Un stationnement de 30 minutes ou moins est gratuit (RM-05).
- **EF-03.3** Entre 7h00 et 19h00, chaque quart d'heure entamé au-delà des 30 minutes gratuites coûte 0,30 € (RM-05). 
- **EF-03.4** Entre 19h00 et 7h00, le forfait de nuit de 3 € s'applique (RM-05, voir Q-01 et Q-02). 
- **EF-03.5** Le montant ne dépasse pas 12 € par période de 24 heures depuis l'entrée (RM-05, voir Q-03).
- **EF-03.6** Le client peut payer en espèces, par carte ou sans contact (paiement simulé).
- **EF-03.7** Après le paiement, le ticket passe au statut « payé », et le paiement (D-03) est enregistré avec son heure.
- **EF-03.8** La caisse calcule le complément d'un ticket dont le délai de sortie est dépassé (RM-06, voir Q-04).

#### Critères d'acceptation

- **EF-03.1** Ticket entré à 10h00, inséré à 11h00 : la caisse affiche 0,60 € (30 minutes payantes, soit 2 quarts d'heure).
- **EF-03.2** Ticket entré à 10h00, inséré à 10h30 : la caisse affiche 0,00 €. Inséré à 10h31 : elle affiche 0,30 €.
- **EF-03.3** Ticket entré à 10h00, inséré à 10h40 : la caisse affiche 0,30 € (10 minutes payantes, 1 quart d'heure entamé). Ce cas a été confirmé par M. Bertrand.
- **EF-03.4** Ticket entré à 20h00, inséré à 6h00 le lendemain : la caisse affiche 3,00 €.
- **EF-03.5** Ticket entré à 7h00, inséré à 19h00 : le calcul donne 13,80 €, la caisse affiche 12,00 €.
- **EF-03.6** Le client paie par carte : le paiement est enregistré avec le mode « carte ».
- **EF-03.7** Après le paiement, le ticket apparaît comme « payé » dans la supervision, avec l'heure du paiement.
- **EF-03.8** Ticket payé à 14h00, inséré à nouveau à 14h20 : la caisse affiche un complément de 0,60 €.

#### Données impliquées

Consulte D-01 ; met à jour le statut de D-01 ; crée D-03.

---

### F-04 - Gérer un ticket perdu

**Acteur(s) :** agent
**Priorité :** souhaitable

#### Description

Un client a perdu son ticket. L'agent retrouve son heure d'entrée à partir de la plaque, déclare le ticket perdu et encaisse le montant dû. Le tarif d'un ticket perdu et la procédure de nuit ne sont pas encore connus (Q-11).

#### Exigences

- **EF-04.1** L'agent recherche un véhicule présent à partir de sa plaque, et retrouve son ticket et son heure d'entrée (D-02).
- **EF-04.2** L'agent déclare le ticket perdu : son statut passe à « perdu » (D-01).
- **EF-04.3** Le montant appliqué à un ticket perdu respecte la règle à définir (Q-11).

#### Critères d'acceptation

- **EF-04.1** Le véhicule 1-ABC-123 est entré à 9h12 : l'agent saisit la plaque et retrouve le ticket entré à 9h12.

#### Données impliquées

Consulte D-02 ; met à jour D-01 ; crée D-03.

---

### F-05 - Encaisser au guichet

**Acteur(s) :** agent
**Priorité :** indispensable

#### Description

L'agent encaisse les clients qui se présentent au guichet. Quand la caisse automatique est en panne pendant ses heures de présence, il passe en mode dégradé : il note chaque paiement à la main avec l'heure réelle, puis l'encode dans le système après la reprise.

#### Exigences

- **EF-05.1** L'agent encaisse un ticket au guichet, avec le même calcul qu'à la caisse automatique (RM-05, RM-06).
- **EF-05.2** L'agent encode a posteriori un paiement noté à la main, en indiquant son heure réelle.
- **EF-05.3** Un paiement encodé a posteriori est identifié comme tel dans la liste des paiements (D-03).
- **EF-05.4** L'agent annule un paiement en indiquant obligatoirement une justification.
- **EF-05.5** Un paiement annulé reste visible dans la liste des paiements, avec sa justification.

Sortie des clients qui ont payé à la main pendant la panne : voir Q-07.

#### Critères d'acceptation

- **EF-05.1** Un ticket entré à 10h00 est encaissé au guichet à 10h40 : le montant affiché est 0,30 €, comme à la caisse automatique.
- **EF-05.2** La caisse est en panne de 10h00 à 11h00. À 11h05, l'agent encode un paiement de 1,20 € noté à 10h20 : le paiement est enregistré avec l'heure 10h20.
- **EF-05.3** Dans la liste des paiements, le paiement de 10h20 porte la mention « encodé a posteriori ».
- **EF-05.4** L'agent tente d'annuler un paiement sans justification : l'annulation est refusée.
- **EF-05.5** Après l'annulation, le paiement apparaît comme « annulé », avec la justification saisie.

#### Données impliquées

Consulte D-01 ; crée et annule des D-03 ; met à jour le statut de D-01.

---

### F-06 - Gérer les abonnés

**Acteur(s) :** agent
**Priorité :** indispensable

#### Description

L'agent inscrit les abonnés au guichet, renouvelle leurs abonnements et remplace les badges perdus. Pour un renouvellement, il vérifie l'identité et le paiement de l'abonné. En cas de perte, il délivre un nouveau badge après vérification, et l'ancien est désactivé immédiatement.

#### Exigences

- **EF-06.1** L'agent inscrit un abonné (D-04) avec une formule « jour » ou « permanent », et lui attribue un badge (RM-08, voir Q-10).
- **EF-06.2** L'agent modifie les coordonnées et les plaques d'un abonné.
- **EF-06.3** L'agent renouvelle un abonnement : la date de fin est prolongée.
- **EF-06.4** L'agent remplace un badge perdu : un nouveau badge est attribué, et l'ancien est désactivé immédiatement.
- **EF-06.5** L'agent met fin à un abonnement : le badge est désactivé.
- **EF-06.6** L'agent consulte la liste des abonnés, avec leur formule et leur date de fin d'abonnement.

#### Critères d'acceptation

- **EF-06.1** L'agent inscrit un abonné « permanent » : son badge permet d'entrer immédiatement (EF-01.3).
- **EF-06.2** Après l'ajout d'une seconde plaque, la fiche de l'abonné affiche les deux plaques.
- **EF-06.3** Un abonnement qui se termine le 31/10 est renouvelé : le badge reste accepté le 01/11.
- **EF-06.4** Juste après le remplacement, l'ancien badge est refusé à l'entrée et le nouveau est accepté.
- **EF-06.5** Après la fin d'un abonnement, le badge est refusé à l'entrée.
- **EF-06.6** La liste affiche chaque abonné avec sa formule et sa date de fin.

#### Données impliquées

Crée, consulte et modifie des D-04.

---

### F-07 - Superviser le parking

**Acteur(s) :** agent, directeur
**Priorité :** indispensable

#### Description

Le directeur et les agents suivent l'activité du parking depuis le guichet : occupation, passages, paiements, véhicules présents et incidents. La supervision se fait sur place (supervision à distance : voir Q-17).

#### Exigences

- **EF-07.1** La supervision affiche le nombre de places occupées et libres, séparément pour les places publiques et les places abonnés (RM-02, D-05).
- **EF-07.2** La supervision affiche les passages d'une journée choisie, avec l'heure, le sens, la plaque, et le ticket ou le badge (D-02).
- **EF-07.3** La supervision affiche les paiements d'une journée choisie, avec le montant, le mode et le lieu d'encaissement (D-03).
- **EF-07.4** La supervision affiche la liste des véhicules présents dans le parking.
- **EF-07.5** La supervision affiche les incidents non résolus (D-07).
- **EF-07.6** L'agent peut corriger le nombre de places occupées, en indiquant une justification (D-05).

Délai de mise à jour de l'affichage : voir Q-15.

#### Critères d'acceptation

- **EF-07.1** Avec 150 clients horaires et 20 abonnés présents, la supervision affiche 40 places publiques libres et 10 places abonnés libres.
- **EF-07.2** Pour le 15/10, la supervision affiche tous les passages de cette journée, et uniquement ceux-là.
- **EF-07.3** Pour le 15/10, la supervision affiche tous les paiements de cette journée, avec leur mode et leur lieu.
- **EF-07.4** Un véhicule entré à 9h00 et pas encore sorti apparaît dans la liste ; un véhicule sorti n'y apparaît plus.
- **EF-07.5** Un incident ouvert apparaît ; après sa résolution (EF-09.3), il disparaît de la liste des incidents non résolus.
- **EF-07.6** Une correction sans justification est refusée.

#### Données impliquées

Consulte D-01, D-02, D-03, D-04, D-05 et D-07 ; corrige D-05.

---

### F-08 - Clôturer la caisse

**Acteur(s) :** agent
**Priorité :** indispensable

#### Description

Chaque soir, l'agent clôture la caisse : le système calcule le total théorique par mode de paiement, l'agent saisit le montant réellement compté, et le système calcule l'écart. Clôture du week-end et procédure en cas d'écart : voir Q-12.

#### Exigences

- **EF-08.1** Le système calcule le total théorique de la journée pour chaque mode de paiement (D-03).
- **EF-08.2** L'agent saisit le montant compté.
- **EF-08.3** Le système calcule et affiche l'écart entre le total théorique et le montant compté.
- **EF-08.4** Une clôture validée ne peut plus être modifiée (D-06).
- **EF-08.5** Un écart différent de zéro crée un incident (F-09).

#### Critères d'acceptation

- **EF-08.1** Pour une journée avec 3 paiements en espèces de 1,20 €, 0,60 € et 3,00 €, le total théorique en espèces est de 4,80 €.
- **EF-08.2** L'agent saisit 4,80 € : le montant est enregistré dans la clôture.
- **EF-08.3** Total théorique en espèces de 4,80 €, montant compté de 4,50 € : l'écart affiché est de -0,30 €.
- **EF-08.4** Après validation, toute tentative de modifier la clôture est refusée.
- **EF-08.5** L'écart de -0,30 € apparaît comme incident dans la supervision (EF-07.5).

#### Données impliquées

Consulte D-03 ; crée D-06 ; crée D-07 en cas d'écart.

---

### F-09 - Tracer les incidents

**Acteur(s) :** agent, directeur
**Priorité :** indispensable

#### Description

M. Bertrand veut être informé de tout événement qui empêche un client d'entrer, de payer ou de sortir normalement. Pour chaque incident, il veut savoir ce qui s'est passé, à quelle heure, et ce qui a été fait pour le résoudre. Information du directeur en dehors de ses heures de présence : voir Q-16.

#### Exigences

- **EF-09.1** Le système enregistre un incident (D-07) dans chacun des cas suivants :
  - une barrière ne se lève pas ;
  - une borne refuse un paiement ;
  - un ticket est illisible ;
  - un badge ne fonctionne pas ;
  - un écart de caisse est constaté (EF-08.5) ;
  - le panneau d'affichage tombe en panne ;
  - la caisse automatique tombe en panne.
- **EF-09.2** Chaque incident indique la date, l'heure, l'équipement concerné et une description.
- **EF-09.3** L'agent indique l'action réalisée et marque l'incident comme résolu.
- **EF-09.4** Le directeur consulte l'historique des incidents, résolus ou non.
- **EF-09.5** Un incident ne peut pas être supprimé.

Panne de la caisse la nuit ou le week-end, sans agent : voir Q-06.

#### Critères d'acceptation

- **EF-09.1** On simule une barrière de sortie qui ne se lève pas à 22h14 : un incident apparaît dans la supervision.
- **EF-09.2** L'incident affiche la date, 22h14, « barrière de sortie » et la description du problème.
- **EF-09.3** Le lendemain, l'agent saisit « barrière redémarrée » et résout l'incident : il apparaît comme résolu, avec l'action réalisée.
- **EF-09.4** Le directeur voit l'incident du 22h14 dans l'historique, avec l'action réalisée.
- **EF-09.5** Aucune action ne permet de supprimer un incident.

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

Charge estimée : 4 étudiants × 30 heures = 120 heures de travail.

# 6. Livrables et planning

## 6.1. Livrables

- **L-01** L'application, installée sur le serveur local, avec la simulation des équipements du site.
- **L-02** Une procédure pratique pour le directeur et les agents : courte et rapide à consulter, couvrant l'utilisation courante et les cas de panne (caisse en panne, mode dégradé).
- **L-03** La formation du directeur et des 2 agents : guichet, caisse, bornes, supervision et mode dégradé. Le contenu est proposé au client, qui le valide.
- **L-04** Le code source et sa documentation technique.

## 6.2. Échéances

| Semaine | Date | Échéance |
| --- | --- | --- |
| S5 | 12/10 | Remise du cahier des charges, validation par M. Bertrand |
| S6 | 19/10 | Conception : diagrammes UML |
| - | 26/10 | Congé de Toussaint |
| S7 | 02/11 | Démo du MVP sur GitHub : F-01, F-02 et F-03 (entrées, sorties, paiement à la caisse) |
| S8 | 09/11 | Spécifications détaillées |
| S8 – S9 | 09/11 – 16/11 | Développement du second incrément : F-05, F-06, F-07, F-08 et F-09 |
| S10 | 23/11 | Démo du second incrément |
| S11 | 30/11 | Tests : vérification des critères d'acceptation et des exigences non fonctionnelles |
| S12 | 07/12 | Version finale (F-04 si le temps le permet), démo client, formation (L-03), procédure (L-02), mise en production et recette finale |

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
