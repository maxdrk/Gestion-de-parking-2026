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

