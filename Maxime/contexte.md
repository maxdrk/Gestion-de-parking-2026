# Cahier de charges Gestion de parkings Valmont

- Auteur : 
1. Maxime Derick
2. gregory Kabasele 
3. Liam Bruyère 
4. Vlad ?
- Version : V1


# Convention d'identification

| Element | Format | Exemple |
| ------- | -------| --------|



## Contexte

Actuellement, l'ensemble du système de gestion repose exclusivement sur une architecture 100 % Cloud. Cette dépendance présente un risque majeur pour la continuité de service : le moindre problème d'accès au réseau provoque une panne totale des installations.

Dernier incident marquant (Mars 2026) : Des travaux de voierie ont causé une coupure Internet de 48 heures. Durant cette période, le système est devenu entièrement indisponible, entraînant une perte d'exploitation estimée à 6 000 €.

### Présentation du client 

- Client : Jean-Luc Bértrand (Directeur d'exploitation)
- Préstataire : 
            1. Maxime Derick
            2. Gregory Kabasele 
            3. Liam Bruyère
            4. Vlad ?

### Présentation du projet

- Problématique : Actuellement, l'ensemble du système de gestion repose exclusivement sur une architecture 100 % Cloud. Cette dépendance présente un risque majeur pour la continuité de service : le moindre problème d'accès au réseau provoque une panne totale des installations.


### Objectif du projet

Pour garantir la résilience et la continuité de l'activité, la Régie des Parkings souhaite migrer vers une solution moderne répondant aux critères suivants :
Fonctionnement en Local : Le système doit impérativement continuer de fonctionner en autonomie locale (gestion des accès, paiements en borne, entrées/sorties) même en cas de perte de la connexion Internet.
Supervision & Interface Réduite/Claire : Une interface de pilotage intuitive offrant une vision en temps réel :
Du suivi détaillé de chaque entrée et sortie client.
De l'état des paiements (tickets horodateurs, paiements en borne).
De la gestion et du suivi des abonnés.