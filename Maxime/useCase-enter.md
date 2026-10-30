| Rubrique | Contenu |
|---|---|
| Identifiant | F-01 |
| Nom | Entrer dans le parking |
| Auteur | Maxime Derick |
| Acteur principal | Client |
| Objectif | Permettre au client d'accéder au parking et de générer un ticket de stationnement. |
| Déclencheur | Le client se présente devant la borne d'entrée du parking. |
| Préconditions | - Le client se présente avec son véhicule devant la borne.<br>- Au moins une place de stationnement est disponible. |
| Postconditions (succès) | - Un ticket unique est généré.<br>- Le ticket est enregistré dans la base de données avec son heure d'entrée.<br>- La barrière d'entrée s'ouvre. |
| Postconditions (échec) | - Aucun ticket n'est généré.<br>- La barrière reste fermée.<br>- L'incident est signalé afin de permettre une intervention. |
| Cas liés | F-06 Gérer les abonnés ; F-07 Superviser le parking ; F-09 Tracer les incidents. |

## Scénario nominal

| Étape | Action |
|---|---|
| 1 | Le client appuie sur le bouton de génération d'un ticket. |
| 2 | Le système vérifie la disponibilité des places. |
| 3 | Le système génère un ticket avec un identifiant unique et enregistre l'heure d'entrée. |
| 4 | Le système commande l'ouverture de la barrière. |
| 5 | Le client récupère son ticket et entre dans le parking. |

## Scénarios alternatifs

### A1 – Gestion des abonnés

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | L'abonné présente son badge devant le lecteur. | Le système identifie le badge et vérifie sa validité. |
| 2 | - | Le système vérifie la formule d'abonnement associée au badge. |
| 3 | - | Si l'abonnement est permanent, l'accès est autorisé sans restriction horaire ni limite de durée. |
| 4 | - | Si l'abonnement est jour, le système vérifie que l'accès a lieu du lundi au vendredi, entre 7 h et 19 h. |
| 5 | - | Si les conditions d'accès sont respectées, l'entrée est enregistrée et la barrière s'ouvre. |
| 6 | - | Si l'abonné jour se présente en dehors de sa plage horaire, le système applique les conditions de tarification normale. |

### A2 – Badge expiré ou invalide

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | L'abonné présente son badge. | Le système détecte que le badge est expiré ou invalide. |
| 2 | - | Le système refuse l'accès par abonnement et informe le client. |
| 3 | Le client appuie sur le bouton de génération d'un ticket. | Le système reprend le scénario nominal d'un client classique. |

### A3 – Parking complet

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | Le client demande l'accès au parking. | Le système constate que les 220 places sont occupées. |
| 2 | - | Le système informe le client que le parking est complet. |
| 3 | - | La barrière reste fermée. |

### A4 – Problème technique

| Étape | Action de l'acteur | Réaction du système |
|---|---|---|
| 1 | Le client tente d'obtenir un ticket ou de présenter son badge. | Le système détecte une anomalie empêchant le traitement de la demande. |
| 2 | Le client contacte l'agent d'accueil ou utilise l'interphone. | L'incident est signalé pour permettre une intervention. |
| 3 | L'agent intervient si nécessaire. | L'accès est autorisé uniquement après résolution du problème et vérification des conditions d'accès. |