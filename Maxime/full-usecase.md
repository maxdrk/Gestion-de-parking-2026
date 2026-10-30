# Diagramme et fiche use case

## Diagramme use case

<img width="627" height="622" alt="DIAGRAM USE CASE PARKING" src="https://github.com/user-attachments/assets/17515c7a-ebc1-4996-8edf-0dc3ee133973" />

## Fiches use case

### Fiche Use Case F-01 : Entrée du parking (Maxime Derick)

| Rubrique | Contenu |
|---|---|
| Identifiant | F-01 |
| Nom | Entrer dans le parking |
| Auteur | Maxime Derick |
| Acteur principal | Client |
| Objectif | Permettre au client d'accéder au parking et de générer un ticket de stationnement. |
| Déclencheur | Le client se présente devant la borne d'entrée du parking. |
| Préconditions | - Le client se présente avec son véhicule devant la borne.<br>- Au moins une place de stationnement est disponible. |
| Postconditions (succès) | - Un ticket unique est généré.<br>- Le ticket est enregistré dans la base de données avec son heure d'entrée.<br> - La plaque est enregistré dans la base de données<br>- La barrière d'entrée s'ouvre. |
| Postconditions (échec) | - Aucun ticket n'est généré.<br>- La barrière reste fermée.<br>- L'incident est signalé afin de permettre une intervention. |
| Cas liés | F-06 Gérer les abonnés ; F-07 Superviser le parking ; F-09 Tracer les incidents. |

#### Scénario nominal

| Étape | Action |
|---|---|
| 1 | Le client appuie sur le bouton de génération d'un ticket. |
| 2 | Le système vérifie la disponibilité des places. |
| 3 | Le système génère un ticket avec un identifiant unique et enregistre l'heure d'entrée. La plaque est également enregistré dans la base de données en cas de perte de ticket. |
| 4 | Le système commande l'ouverture de la barrière. |
| 5 | Le client récupère son ticket et entre dans le parking. |

#### Scénarios alternatifs

##### A1 : Gestion des abonnés

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | L'abonné présente son badge devant le lecteur. | Le système identifie le badge et vérifie sa validité. |
| 2 | / | Le système vérifie la formule d'abonnement associée au badge. |
| 3 | / | Si l'abonnement est permanent, l'accès est autorisé sans restriction horaire ni limite de durée. |
| 4 | / | Si l'abonnement est jour, le système vérifie que l'accès a lieu du lundi au vendredi, entre 7 h et 19 h. |
| 5 | / | Si les conditions d'accès sont respectées, l'entrée est enregistrée et la barrière s'ouvre. |
| 6 | / | Si l'abonné jour se présente en dehors de sa plage horaire, le système applique les conditions de tarification normale. |

##### A2 : Badge expiré ou invalide

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | L'abonné présente son badge. | Le système détecte que le badge est expiré ou invalide. |
| 2 | / | Le système refuse l'accès par abonnement et informe le client. |
| 3 | Le client appuie sur le bouton de génération d'un ticket. | Le système reprend le scénario nominal d'un client classique. |

##### A3 : Parking complet

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | Le client demande l'accès au parking. | Le système constate que les 220 places sont occupées. |
| 2 | / | Le système informe le client que le parking est complet. |
| 3 | / | La barrière reste fermée. |

##### A4 : Problème technique

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | Le client tente d'obtenir un ticket ou de présenter son badge. | Le système détecte une anomalie empêchant le traitement de la demande. |
| 2 | Le client contacte l'agent d'accueil ou utilise l'interphone. | L'incident est signalé pour permettre une intervention. |
| 3 | L'agent intervient si nécessaire. | L'accès est autorisé uniquement après résolution du problème et vérification des conditions d'accès. |

### Justification fiche case F-01

L'entrée du parking constitue un point essentiel du fonctionnement du système. Elle représente le premier contact entre l'utilisateur et le parking et permet d'initier une session de stationnement.

Ce cas d'utilisation est indispensable puisqu'il permet de gérer l'accès des clients occasionnels et des abonnés, de vérifier leurs droits d'accès et d'enregistrer chaque entrée. Sans ce processus, le système ne pourrait pas assurer le suivi des véhicules, la gestion des stationnements ni la facturation des clients.
---
### Fiche Use Case F-02 : Sortie du parking (Maxime Derick)

#### 1. Informations générales

| Rubrique | Contenu |
|---|---|
| Identifiant | F-02 |
| Nom | Sortie du parking |
| Auteur | Maxime Derick |
| Acteur principal | Client |
| Acteurs secondaires | Agent d'accueil |
| Objectif | Permettre au client de régler son stationnement et de quitter le parking. |
| Déclencheur | Le client se présente devant la borne de paiement ou de sortie avec son ticket. |
| Préconditions | - Le client possède un ticket de stationnement valide.<br>- Une entrée correspondant au ticket est enregistrée dans le système. |
| Postconditions (succès) | - Le paiement du stationnement est enregistré.<br>- La sortie du véhicule est enregistrée dans la base de données.<br>- La barrière de sortie s'ouvre. |
| Postconditions (échec) | - La barrière reste fermée.<br>- Le paiement ou la sortie n'est pas validé.<br>- Un incident peut être signalé à l'agent d'accueil ou via l'interphone. |
| Cas liés | F-01 Entrée du parking ; F-07 Superviser le parking ; F-09 Tracer les incidents. |

#### 2. Scénario nominal : Paiement et sortie

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | Le client se présente à la borne de paiement et insère son ticket. | Le système lit l'identifiant du ticket. |
| 2 | / | Le système récupère l'heure d'entrée et calcule la durée du stationnement. |
| 3 | / | Le système calcule le montant à payer selon la grille tarifaire en vigueur. |
| 4 | Le client effectue le paiement. | Le système valide et enregistre le paiement. |
| 5 | Le client se présente à la borne de sortie et insère son ticket payé. | Le système vérifie que le paiement a été effectué et que le délai de sortie de 15 minutes n'est pas dépassé. |
| 6 | / | Le système autorise l'ouverture de la barrière. |
| 7 | Le client quitte le parking. | Le système enregistre l'heure de sortie et libère une place de stationnement. |

#### 3. Scénarios alternatifs

##### A1 : Dépassement du délai de sortie

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | Le client présente son ticket payé à la borne de sortie. | Le système constate que le délai de 15 minutes est dépassé. |
| 2 | / | Le système refuse l'ouverture de la barrière et informe le client. |
| 3 | Le client effectue un paiement complémentaire. | Le système calcule le supplément depuis l'heure du paiement précédent, sans appliquer les 30 minutes gratuites. |
| 4 | / | Le système valide le paiement complémentaire et autorise la sortie. |

##### A2 : Ticket perdu

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | Le client signale la perte de son ticket à l'agent d'accueil ou via l'interphone. | Le système permet à l'agent de rechercher le véhicule à partir de sa plaque d'immatriculation. |
| 2 | / | Si l'heure d'entrée est retrouvée grâce à la plaque enregistrée par la caméra, le système calcule le tarif normal. |
| 3 | / | Si l'heure d'entrée ne peut pas être retrouvée, un forfait de 25 € est appliqué. |
| 4 | Le client effectue le paiement. | Le système enregistre le paiement et permet la sortie du véhicule. |

##### A3 : Paiement refusé

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | Le client tente d'effectuer le paiement. | Le système détecte que la transaction est refusée. |
| 2 | / | Le système informe le client que le paiement n'a pas été validé. |
| 3 | Le client tente un autre moyen de paiement ou contacte l'agent. | Le système attend la validation du paiement avant d'autoriser la sortie. |

#### 4. Règles métier associées

| Référence | Description |
|---|---|
| RM-05 à RM-08 | Tarification horaire, tarif de nuit et plafond de 12 € par période de 24 heures. |
| RM-09 | Gestion des tickets perdus et application du forfait de 25 € si l'heure d'entrée ne peut pas être retrouvée. |
| RM-10 | Le client dispose de 15 minutes après le paiement pour quitter le parking. |
| RM-11 | Au-delà du délai de sortie, un supplément est calculé depuis l'heure du paiement précédent, sans les 30 minutes gratuites. |

---

### Fiche Use Case F-05 : Encaisser au guichet (auteur : Liam Bruyère)

| Rubrique                    | Contenu                                                                                                                                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Identifiant**             | F-05                                                                                                                                                                                            |
| **Nom**                     | Encaisser au guichet                                                                                                                                                                            |
| **Auteur**                  | Liam Bruyère                                                                                                                                                                                    |
| **Acteur principal**        | Agent d'accueil                                                                                                                                                                                 |
| **Priorité**                | Indispensable                                                                                                                                                                                   |
| **Objectif**                | Encaisser le ticket d'un client horaire qui se présente au guichet, afin qu'il puisse sortir du parking.                                                                                        |
| **Déclencheur**             | Un client horaire présente son ticket au guichet.                                                                                                                                               |
| **Préconditions**           | L'agent est présent et connecté au système (lundi au vendredi, 7h00 à 19h00, RM-03). Le client possède un ticket au statut « en cours ».                                                        |
| **Postconditions (succès)** | Un paiement (D-03) est enregistré avec son montant, son mode, son heure et le lieu « guichet ». Le ticket (D-01) passe au statut « payé ». Le client dispose de 15 minutes pour sortir (RM-06). |
| **Postconditions (échec)**  | Aucun paiement n'est enregistré et le statut du ticket ne change pas.                                                                                                                           |
| **Cas liés**                | Inclus par F-04 _Gérer un ticket perdu_ (l'agent encaisse le montant dû). Utilise le même calcul tarifaire que F-03 _Payer à la caisse automatique_.                                            |

#### Scénario nominal : Entrer dans le parking

1. le client remet son ticket à l'agent 
2. l'agent saisit le numéro du ticket dans le système 
3. le système affiche l'heure d'entrée et calcule le montant selon le tarif (RM-05), avec le même calcule qu'à la caisse automatique 
4. l'agent annonce le montant au client 
5. le client paie en espèces, par carte ou sans contact (paiement simulé) 
6. l'agent sélectionne le mode de paiement  et valide l'encaissement 
7. le système enregistre le paiement avec le lieu "guichet" et l'heure du paiement puis passe le ticket au statut "payé"
8. le système confirme l'encaissement ; l'agent rend le ticket au client 

**exemple** : le ticket  entré à 10H00, encaissé a 10H40. le système affiche 0,30 € (30 minutes gratuites, puis 1 quart d'heure entamé). Après validation, le ticket apparaît "payé" dans la supervision 

#### Scénarios alternatifs

##### 3a. Stationnement de 30 minutes ou moins

- 3a.1 le système affiche 0,00 €.
- 3a.2 l'agent valide sans encaissement : le ticket passe au statut "payé". retour a l'étape 8 

##### 3b. Ticket déjà payé mais délai de sortie de 15 minutes dépassé

- 3b.1 Le système calcule le complément depuis l'heure du premier paiement (RM-06, EF-03.8).
- 3b.2 Le scénario reprend à l'étape 4 avec le montant du complément.

##### 5a. Le client ne peut pas ou ne veut pas payer

- 5a.1 l'agent annule l'opération
- 5a.2 Aucun paiement n'est enregistré; le ticket reste "en cours" fin du cas (échec) 

##### 6a. Caisse automatique en panne ; mode dégradé (EF-05.2, EF-05.3)

- 6a.1pendannt la pane, l'agent encaisse et note chaque paiement à la main avec l'heure réelle. 
- 6a.2 après la reprise, l'agent ouvre l'encodage a posteriori et saisit le numéro du ticket, le montant, le mode et l'heure réelle du paiement. 
- 6a.3 le système enregistre le paiement à l'heure indiqué et le marque "encodé a posteriori"

##### 8a. Erreur d'encaissement découverte après validation (EF-05.4, EF-05.5)

- 8a.1 l'agent  sélectionne le paiement et demande son annulation. 
- 8a.2 le système exige une justification
- 8a.3 l'agent saisit la justification et confirme 
- 8a.4 le système marque  le paiement "annulé" ; il reste visible dans la liste des paiement avec sa justification. le ticket repasse au statut "en cours"

#### Exceptions

**2a. Numéro de ticket inconnu ou illisible**

- 2a.1 Le système affiche « ticket introuvable ».
- 2a.2 L'agent ressaisit le numéro. Si le ticket reste introuvable, il bascule vers F-04 _Gérer un ticket perdu_.

**2b. Ticket déjà utilisé pour sortir**

- 2b.1 Le système refuse l'encaissement et affiche « ticket déjà utilisé ». Fin du cas (échec).

**8b. Annulation sans justification**

- 8b.1 Le système refuse l'annulation tant qu'aucune justification n'est saisie.

#### Règles métier et données

- **Règles métier** : RM-03 (présence de l'agent), RM-05 (tarif : 30 min gratuites, 0,30 € par quart d'heure entamé de 7h à 19h, forfait de nuit de 3 €, maximum 12 € par 24 h), RM-06 (15 minutes pour sortir après paiement).
- **Données** : consulte D-01 _Ticket_ ; crée et annule des D-03 _Paiement_ ; met à jour le statut de D-01.
- **Exigences couvertes** : EF-05.1 à EF-05.5.

#### Questions ouvertes

- **Q-04** : le complément après dépassement des 15 minutes compte-t-il dans le maximum de 12 € ?
- **Q-07** : pendant une panne de caisse, comment sortent les clients qui ont payé à la main avant l'encodage a posteriori ?

---

### Fiche Use Case F-06 : Gérer les abonnés (auteur : Liam Bruyère)

| Rubrique                    | Contenu                                                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Identifiant**             | F-06                                                                                                                                                             |
| **Acteur principal**        | Agent d'accueil                                                                                                                                                  |
| **Priorité**                | Indispensable                                                                                                                                                    |
| **Objectif**                | Inscrire, modifier, renouveler ou clôturer l'abonnement d'un client, et gérer son badge.                                                                         |
| **Déclencheur**             | Un client (ou futur abonné) se présente au guichet.                                                                                                              |
| **Préconditions**           | L'agent est présent et connecté (RM-03).                                                                                                                         |
| **Postconditions (succès)** | La fiche abonné (D-04) est créée ou mise à jour ; le badge est actif ou désactivé selon l'action. Le changement est pris en compte immédiatement par les bornes. |
| **Postconditions (échec)**  | La fiche abonné n'est pas modifiée.                                                                                                                              |

#### Scénario nominal : inscrire un abonné

1. Le client demande un abonnement.
2. L'agent ouvre le formulaire d'inscription.
3. L'agent saisit le nom, les coordonnées, la ou les plaques et la formule (« jour » ou « permanent »).
4. L'agent vérifie l'identité et le paiement de l'abonnement.
5. L'agent attribue un badge au client.
6. Le système enregistre l'abonné (D-04) avec ses dates d'abonnement et le badge au statut « actif ».
7. L'agent remet le badge au client.

**Exemple** : un abonné « permanent » est inscrit ; son badge lui permet d'entrer immédiatement (EF-01.3).

#### Scénarios alternatifs

**2a. Renouveler un abonnement**

- 2a.1 L'agent recherche l'abonné et vérifie son identité et son paiement.
- 2a.2 L'agent prolonge l'abonnement ; le système met à jour la date de fin.
- Exemple : un abonnement qui finit le 31/10 est renouvelé ; le badge reste accepté le 01/11.

**2b. Modifier les coordonnées ou les plaques**

- L'agent modifie la fiche ; après l'ajout d'une seconde plaque, la fiche affiche les deux plaques.

**2c. Remplacer un badge perdu**

- 2c.1 L'agent vérifie l'identité de l'abonné.
- 2c.2 L'agent attribue un nouveau badge ; le système désactive immédiatement l'ancien.
- L'ancien badge est refusé à l'entrée, le nouveau est accepté.

**2d. Mettre fin à un abonnement**

- L'agent met fin à l'abonnement ; le système désactive le badge, qui est ensuite refusé à l'entrée.

**2e. Consulter la liste des abonnés**

- Le système affiche chaque abonné avec sa formule et sa date de fin.

#### Exceptions

**3a. Champ obligatoire manquant** : le système refuse l'enregistrement et indique le champ à compléter. **5a. Numéro de badge déjà attribué** : le système refuse ; l'agent choisit un autre badge (numéro de badge unique, D-04). **4a. Identité ou paiement non vérifiés** : l'agent annule l'opération.

#### Règles et données

RM-08 ; crée, consulte et modifie D-04. Données personnelles soumises au RGPD (ENF-06). Exigences EF-06.1 à EF-06.6.

#### Questions ouvertes

Q-10 (heures de la formule « jour », prix, nombre d'abonnés), Q-13 (durée de conservation).