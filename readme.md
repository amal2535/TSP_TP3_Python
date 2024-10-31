# Projet : Problème du Voyageur de Commerce avec Contraintes (TSP)

Ce projet implémente une solution avancée au problème du voyageur de commerce (TSP) en utilisant la bibliothèque OR-Tools de Google. Il prend en compte des contraintes réelles telles que les fenêtres temporelles, les capacités de véhicule, les routes impraticables et les arrêts obligatoires, rendant la solution plus adaptée aux applications de logistique et de planification de parcours.

## Objectif

Le but de ce projet est de trouver le chemin optimal pour qu'un voyageur visite un ensemble de villes une seule fois, puis retourne à sa ville de départ, tout en respectant :
1. Les fenêtres temporelles de chaque ville.
2. La capacité du véhicule pour le transport de marchandises.
3. Les routes impraticables entre certaines villes.
4. La nécessité d’arrêts obligatoires pour le repos après une certaine distance.

L'objectif est de minimiser la distance totale parcourue.

## Fonctionnalités

- **Optimisation des routes** : Calcul de l'itinéraire optimal en minimisant la distance ou le temps total.
- **Fenêtres temporelles** : Visite de chaque ville dans une plage de temps spécifique.
- **Capacité du véhicule** : Gestion de la charge de marchandises transportées par le voyageur.
- **Routes impraticables** : Exclusion des connexions entre certaines villes.
- **Arrêts de repos obligatoires** : Ajout de pauses après un certain nombre de kilomètres parcourus.

## Prérequis

- Python 3.6 ou supérieur
- [Poetry](https://python-poetry.org/) pour la gestion des dépendances


