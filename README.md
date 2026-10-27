# Gestion de paiement 

## Tarification du stationnement

Selon la grille tarifaire issue de la délibération de décembre 2024 :

- Les 30 premières minutes de stationnement sont gratuites.
- De 7 h à 19 h, chaque quart d’heure commencé après la période gratuite est facturé 0,30 €.
- De 19 h à 7 h, un forfait de nuit de 3 € s’applique.
- Le montant est plafonné à 12 € par période de 24 heures, calculée à partir de l’heure d’entrée.

Le montant dû est calculé à la sortie à partir des heures d’entrée et de sortie du ticket.

## Ce qui est fait pour le moment 

- main.py : Lance une connexion à la base de donnée pour ensuite appelé le fichier getTicket et sa fonction getTickets en y injectant la connexion et l'id du demandé qui a été demandé
- getTicket : Récupère le fichier et l'id Récupère l'heure d'entrée et de sortie pour ensuite les soustraire et donnéez la durée total 

## Ce qui manque à faire 

- Faire la grille tarifaire afin de déterminer le montant à payer en fonction de la durée obtenu 
- Eventuellemnt préparer un runner pour les appareils sous Macos,Linux (encore à tester)
# Exemple

![alt text](photos/image.png)