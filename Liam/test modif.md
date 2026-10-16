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

|Code|Donnée|Contenu|Origine|Volume|Conservation / confidentialité|Opérations (acteur, fonctionnalité)|
|---|---|---|---|---|---|---|
|D-01|Ticket|N° de ticket (unique), date et heure d'entrée, plaque, statut (en cours, payé, perdu)|Borne d'entrée|[X par jour]|[Durée à définir] ; contient une plaque (donnée personnelle)|Créer : borne d'entrée (F-01) ; Consulter : agent, borne de sortie, caisse auto (F-02 à F-05) ; Marquer payé : caisse auto, agent (F-03, F-05) ; Déclarer perdu : agent (F-04)|
|D-02|Passage|Date et heure, sens (entrée/sortie), plaque lue, ticket (D-01) ou badge (D-04), borne|Bornes d'entrée et de sortie|[~2 par ticket ou trajet d'abonné]|[Durée à définir], puis anonymisation de la plaque (RGPD)|Enregistrer : bornes (F-01, F-02) ; Consulter : agent pour ticket perdu, superviseur (F-04, F-07) ; jamais modifié|
|D-03|Paiement|Montant, mode (espèces, carte, sans contact), date et heure, ticket (D-01), lieu d'encaissement|Caisse auto, agent|[X par jour]|[Durée légale comptable à vérifier] ; aucune donnée de carte bancaire conservée|Enregistrer : caisse auto, agent (F-03, F-05) ; Consulter : agent, superviseur (F-07, F-08) ; Annuler : agent avec justification (F-05)|
|D-04|Abonné|Nom, coordonnées, plaque(s), type et dates d'abonnement, n° de badge (unique), statut du badge (actif, bloqué)|[Reprise du système Cloud ?], puis agent|[Nombre d'abonnés ?]|[Durée après fin d'abonnement], puis anonymisation ; donnée personnelle|Inscrire, modifier, renouveler, bloquer/débloquer le badge, mettre fin : agent (F-06) ; Consulter : agent, bornes pour vérifier le badge (F-01, F-02, F-06)|
|D-05|Occupation|Capacité totale (RM-02), places occupées, places restantes|Calculée par le système à partir des passages|Temps réel|[Historique à garder ?]|Mettre à jour : système (F-01, F-02) ; Consulter : clients via panneau, agent, superviseur (F-07) ; Corriger : agent (F-07)|
|D-06|Clôture de caisse|Date, agent, total théorique par mode de paiement, montant compté, écart|Agent|[1 par jour ouvrable ?]|[Durée légale comptable à vérifier]|Créer, valider : agent (F-08) ; Consulter : agent, superviseur (F-07, F-08) ; non modifiable une fois validée|