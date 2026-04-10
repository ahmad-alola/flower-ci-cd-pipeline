# Déploiement

## Objectif du pipeline

Le pipeline CI/CD doit automatiser les étapes principales du projet.

## Étapes prévues

1. récupération du code depuis GitHub,
2. installation des dépendances,
3. exécution des tests,
4. construction des images Docker,
5. push des images sur Docker Hub,
6. déploiement ou mise à jour sur Azure.

## Déclenchement

Le pipeline est prévu pour se lancer automatiquement à chaque push sur la branche `main`.

## Docker Hub

Deux images doivent être publiées :

- une image pour le backend,
- une image pour le frontend.

## Azure

Azure doit récupérer les nouvelles images puis redémarrer les applications avec la version la plus récente.


Azure récupère les nouvelles images Docker depuis Docker Hub.

Pour automatiser complètement le déploiement, un webhook est utilisé. Après chaque build et push des images Docker, GitHub Actions envoie une requête HTTP vers Azure.

Cela permet de déclencher automatiquement :

- le téléchargement de la nouvelle image,
- le redémarrage du conteneur,
- la mise à jour de l’application.

Cette solution permet d’éviter un redémarrage manuel et garantit un déploiement continu fiable.

## Intérêt pédagogique

Ce déploiement permet de comprendre comment passer d’un projet local à une application accessible en ligne.

Il permet aussi de voir le lien entre :

- développement,
- tests,
- conteneurisation,
- automatisation,
- cloud.

