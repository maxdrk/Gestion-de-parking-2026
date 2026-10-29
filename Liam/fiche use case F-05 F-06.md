# Fiche Use Case F-05 : Encaisser au guichet (auteur : Liam Bruyère)

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

## scénario nominal 
1. le client remet son ticket à l'agent 
2. l'agent saisit le numéro du ticket dans le système 
3. le système affiche l'heure d'entrée et calcule le montant selon le tarif (RM-05), avec le même calcule qu'à la caisse automatique 
4. l'agent annonce le montant au client 
5. le client paie en espèces, par carte ou sans contact (paiement simulé) 
6. l'agent sélectionne le mode de paiement  et valide l'encaissement 
7. le système enregistre le paiement avec le lieu "guichet" et l'heure du paiement puis passe le ticket au statut "payé"
8. le système confirme l'encaissement ; l'agent rend le ticket au client 
**exemple** : le ticket  entré à 10H00, encaissé a 10H40. le système affiche 0,30 € (30 minutes gratuites, puis 1 quart d'heure entamé). Après validation, le ticket apparaît "payé" dans la supervision 
## scénario alternative 
### 3a. stationnement  de 30 minutes ou moins 
- 3a.1 le système affiche 0,00 €.
- 3a.2 l'agent valide sans encaissement : le ticket passe au statut "payé". retour a l'étape 8 
### 3b. ticket déjà payé mais délai de sortie de 15 minutes dépassé
- 3b.1 Le système calcule le complément depuis l'heure du premier paiement (RM-06, EF-03.8).
- 3b.2 Le scénario reprend à l'étape 4 avec le montant du complément.
### 5a. le client ne peut pas ou ne veut pas payer 
- 5a.1 l'agent annule l'opération
- 5a.2 Aucun paiement n'est enregistré; le ticket reste "en cours" fin du cas (échec) 
### 6a. Caisse automatique en panne; mode dégradé (EF-05.2, EF-05.3) 
- 6a.1pendannt la pane, l'agent encaisse et note chaque paiement à la main avec l'heure réelle. 
- 6a.2 après la reprise, l'agent ouvre l'encodage a posteriori et saisit le numéro du ticket, le montant, le mode et l'heure réelle du paiement. 
- 6a.3 le système enregistre le paiement à l'heure indiqué et le marque "encodé a posteriori"
### 8a Erreur d'encaissement découverte après validation (EF-05.4, EF-05.5) 
- 8a.1 l'agent  sélectionne le paiement et demande son annulation. 
- 8a.2 le système exige une justification
- 8a.3 l'agent saisit la justification et confirme 
- 8a.4 le système marque  le paiement "annulé" ; il reste visible dans la liste des paiement avec sa justification. le ticket repasse au statut "en cours"
## Exceptions

**2a. Numéro de ticket inconnu ou illisible**

- 2a.1 Le système affiche « ticket introuvable ».
- 2a.2 L'agent ressaisit le numéro. Si le ticket reste introuvable, il bascule vers F-04 _Gérer un ticket perdu_.

**2b. Ticket déjà utilisé pour sortir**

- 2b.1 Le système refuse l'encaissement et affiche « ticket déjà utilisé ». Fin du cas (échec).

**8b. Annulation sans justification**

- 8b.1 Le système refuse l'annulation tant qu'aucune justification n'est saisie.

## Règles métier et données

- **Règles métier** : RM-03 (présence de l'agent), RM-05 (tarif : 30 min gratuites, 0,30 € par quart d'heure entamé de 7h à 19h, forfait de nuit de 3 €, maximum 12 € par 24 h), RM-06 (15 minutes pour sortir après paiement).
- **Données** : consulte D-01 _Ticket_ ; crée et annule des D-03 _Paiement_ ; met à jour le statut de D-01.
- **Exigences couvertes** : EF-05.1 à EF-05.5.

## Questions ouvertes

- **Q-04** : le complément après dépassement des 15 minutes compte-t-il dans le maximum de 12 € ?
- **Q-07** : pendant une panne de caisse, comment sortent les clients qui ont payé à la main avant l'encodage a posteriori ?
---

# Fiche Use Case F-06 : Gérer les abonnés (auteur : Liam Bruyère)

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

## Scénario nominal : inscrire un abonné

1. Le client demande un abonnement.
2. L'agent ouvre le formulaire d'inscription.
3. L'agent saisit le nom, les coordonnées, la ou les plaques et la formule (« jour » ou « permanent »).
4. L'agent vérifie l'identité et le paiement de l'abonnement.
5. L'agent attribue un badge au client.
6. Le système enregistre l'abonné (D-04) avec ses dates d'abonnement et le badge au statut « actif ».
7. L'agent remet le badge au client.

**Exemple** : un abonné « permanent » est inscrit ; son badge lui permet d'entrer immédiatement (EF-01.3).

## Scénarios alternatifs

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

## Exceptions

**3a. Champ obligatoire manquant** : le système refuse l'enregistrement et indique le champ à compléter. **5a. Numéro de badge déjà attribué** : le système refuse ; l'agent choisit un autre badge (numéro de badge unique, D-04). **4a. Identité ou paiement non vérifiés** : l'agent annule l'opération.

**Règles et données** : RM-08 ; crée, consulte et modifie D-04. Données personnelles soumises au RGPD (ENF-06). Exigences EF-06.1 à EF-06.6. **Questions ouvertes** : Q-10 (heures de la formule « jour », prix, nombre d'abonnés), Q-13 (durée de conservation).