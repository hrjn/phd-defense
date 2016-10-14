## Draft plan defense

* Duration: 45 minutes
---
### Contexte, enjeux et problématique

  * Contexte
  * La dispersion atmosphérique
    -> Pas de détails
    -> Insister sur:
	- l'incertitude autour des résultats/modèles
	- leur coût en temps de calcul
  * La source: objet d'intérêt
    -> Définir la formulation mathématique d'une source
  * Le problème STE: un état de l'art
  * Problématique de recherche

---
### Inférence bayésienne et méthodes de Monte-Carlo

  * Principes de base
  * Justification des méthodes MC
  * Présentation du concept MC
  * MCMC
    -> Principe: update d'une chaine de Markov
    -> Metropolis-Hastings
    -> Gibbs
    -> Autres: HMC, etc.
  * IS
    -> Vanilla
    -> PMC
    -> D-kernel PMC et M-PMC
    -> AMIS
      - principes
      - avantages

---
### Estimation de source sur un cas expérimental (1ère contribution)

  Idée: tracer un itinéraire de résolution du problème, et rassembler les 
  outils nécessaires.
  * Formulation bayésienne du problème
  * Démarche de résolution
    -> Badass diagram goes here :-)
    -> Highlight: marginal posterior de la position
    -> Highlight: conditional posterior du profil d'émission
    -> Formulation complète de la joint posterior
  * Calculer la vraisemblance: le modèle de dispersion gaussien
  Maintenant qu'on est équipés, on regarde à quoi on se frotte:
  * Contexte de l'expérience FFT07
  * Résultats et conclusions
    -> Mentionner les papiers concernés

---
### Estimation de source combinée avec un modèle rétrograde (2e contribution) 

  * Problème: souligner les bottlenecks qui apparaissent avec la montée en complexité
  du modèle

  * Solution: avoir recours à un modèle rétrograde pour stocker les matrices SR
    -> Dualité direct/rétrograde
    -> Modifications conséquentes dans le workflow

  * Modèle de dispersion PMSS
    -> Justification: urbain + avec version rétrograde
    -> La dispersion en mode lagrangien

  * Résultats en milieu rural: la simulation BEAUNE
    -> Contexte
    -> Résultats

  * Résultats en milieu urbain: la simulation OPERA
    -> Initialisation améliorée de l'AMIS
    -> Contexte
    -> Résultats

  * Conclusions

---
### Conclusions et perspectives

  * L'approche bayésienne a apporté un bon framework et une méthodo rigoureuse pour 
    proposer une solution au problème STE.
  * Le travail de la thèse a permis d'établir une façon originale/innovante d'estimer
    à la fois la position et le profil temporel d'émission d'une source.
  * Cependant, les différents résultats obtenus durant ces travaux soulèvent également    d'autres questions d'importance:
      -> déploiement optimal du réseau de capteurs (slide entière)
      -> validation de l'approche "rétrograde" sur un cas expérimental
      -> traitement séquentiel des données d'observation (SMC sampler)


--- 

* Merci + questions

---


