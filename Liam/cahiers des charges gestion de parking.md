# Cahier de charges Gestion de parkings Valmont

a

- Auteur :

1. Maxime Derick
2. gregory Kabasele
3. Liam Bruyère
4. Vlad vlad

- Version : V1

# Convention d'identification

| Element          | Format  | Exemple |
| ---------------- | ------- | ------- |
| Règle métier     | RM - XX | RM-01   |
| encore à définir | xxx     | xxx     |

## Contexte

Actuellement, l'ensemble du système de gestion repose exclusivement sur une architecture 100 % Cloud. Cette dépendance présente un risque majeur pour la continuité de service : le moindre problème d'accès au réseau provoque une panne totale des installations.

Dernier incident marquant (Mars 2026) : Des travaux de voierie ont causé une coupure Internet de 48 heures. Durant cette période, le système est devenu entièrement indisponible, entraînant une perte d'exploitation estimée à 6 000 €.

### présentation du client

- Client : Jean-Luc Bertrand (Directeur d'exploitation)
- Prestataire :

1. Maxime Derick
2. Gregory Kabasele
3. Liam Bruyère
4. Vladyslav Volodichev

### Présentation du projet

- Problématique : Actuellement, l'ensemble du système de gestion repose exclusivement sur une architecture 100 % Cloud. Cette dépendance présente un risque majeur pour la continuité de service : le moindre problème d'accès au réseau provoque une panne totale des installations.

### Objectif du projet

Afin de garantir la résilience et la continuité de son activité, la Régie des Parkings souhaite migrer vers une solution moderne répondant à plusieurs critères essentiels.

Tout d’abord, le système doit impérativement pouvoir fonctionner en local. Même en cas de perte de la connexion Internet, il doit continuer d’assurer en toute autonomie la gestion des accès, les paiements en borne ainsi que le contrôle des entrées et des sorties.

Ensuite, la solution doit offrir une interface de supervision claire et épurée, permettant un pilotage intuitif des installations. Cette interface doit fournir une vision en temps réel de l’activité du parking, avec un suivi détaillé de chaque entrée et sortie des clients. Elle doit également permettre de consulter l’état des paiements, qu’il s’agisse des tickets horodateurs ou des transactions effectuées en borne. Enfin, elle doit intégrer la gestion et le suivi des abonnés.és.

## Description générale

L'application de gestion des parkings Valmont est une solution hébergée sur une infrastructure locale, destinée à centraliser et à simplifier la gestion quotidienne des parkings. Elle permet de gérer les informations relatives aux abonnés, aux paiements, aux tickets, ainsi qu'aux entrées et sorties des véhicules.

L'objectif principal de cette solution est de garantir la continuité de service, même en cas de perte de connexion Internet. Contrairement à l'architecture actuelle, qui repose entièrement sur des services Cloud, la nouvelle application doit pouvoir assurer localement les opérations essentielles à l'exploitation des parkings.

Le système doit notamment permettre :

- **La gestion des accès :** suivi des entrées et sorties des véhicules, enregistrement des événements et consultation de l'historique des passages.
- **La gestion des abonnés :** création et modification des dossiers, suivi des abonnements, consultation des périodes de validité et gestion des renouvellements.
- **Le suivi des paiements :** centralisation des informations relatives aux paiements effectués aux bornes et aux tickets horodateurs, avec suivi de leur état.
- **La supervision des parkings :** affichage d'une vue d'ensemble de l'activité, permettant aux opérateurs de consulter rapidement les informations essentielles et de détecter les éventuelles anomalies.
- **Le fonctionnement hors ligne :** maintien des fonctionnalités critiques en cas d'interruption de la connexion Internet, sans dépendance permanente à des services distants.

L'application devra proposer une interface utilisateur claire, intuitive et accessible aux personnes chargées de l'exploitation. Elle devra faciliter la consultation des données, limiter les manipulations inutiles et permettre une prise de décision rapide en cas d'incident.

L'architecture devra également prévoir la conservation locale des données et des mécanismes de sauvegarde afin de limiter les risques de perte d'informations. Si une synchronisation avec des services externes est nécessaire, elle devra pouvoir reprendre après le rétablissement de la connexion Internet, sans provoquer de doublons ni de pertes de données.

Enfin, la solution devra être conçue de manière modulaire afin de faciliter sa maintenance, son évolution et l'ajout éventuel de nouvelles fonctionnalités. Les modalités précises de fonctionnement hors ligne, de synchronisation, de sécurité et d'intégration avec les équipements existants seront définies dans les exigences fonctionnelles et techniques du projet.

## Règles métiers

- RM-01 : horaires d'ouverture : 24/24 7j/7
- RM-02 : capacités 220 places
- RM-03 : présence d'un agent d'acceuil : du lundi au vendredi, de 07H00 à 19h00
- RM-04 : gestion 100% automatisé (bornes et caisses automatiques) le reste du temps (soir, week-ends et jour fériés)

## Périmètre

**Éléments inclus**

Hébergement de l'application sur une infrastructure locale.

Gestion des abonnés, des paiements et des tickets.

Suivi des entrées et sorties des véhicules.

Supervision de l'activité des parkings via une interface centralisée.

Maintien des fonctionnalités essentielles en cas de coupure Internet.

**Éléments exclus**

Hébergement de l'application ou de ses composants sur une infrastructure Cloud accessible via Internet.

## Données

- entrés (donnes un ticket)
- sortie du parking (verification du paiements)
- paiements à la caiss automatique
- verification du paiements
- un agent :
  - aides les clients
  - gère les paiements
  - s’occupe de ticket perdu, il verifie l'heures d'arrivé des véhicules grâce a leurs plaque
  - lorsque le système tombe en panne il s’occupe des paiements
- gestion des abonnées avec badges
- comptages et affichage des places réstante
- cloture des caisses avec vérification du total par mode de paiemen et l'écart avec la caisse réelle

> Utilisation de Claude et ChatGPT (GPT-6) pour reformuler et structurer les idées recueillies lors des échanges avec Monsieur Bertrand.
