# Architecture du projet

## Vue d’ensemble

Le projet suit une architecture simple en plusieurs étapes.

```text
Dataset -> Training -> Model artifact -> API FastAPI -> Frontend Streamlit -> Docker -> GitHub Actions -> Docker Hub -> Azure
```

## 1. Données

Les données viennent du dataset Iris.

Deux approches ont été utilisées :

- chargement direct depuis `scikit-learn`,
- utilisation d’un fichier CSV dans le projet.

Le notebook permet d’explorer les données, de vérifier leur structure et de faire une petite analyse.

## 2. Entraînement

Le fichier `backend/train.py` permet de :

- charger les données,
- nettoyer les doublons et les valeurs manquantes,
- séparer les données en train et test,
- entraîner un modèle,
- mesurer la performance,
- enregistrer les informations avec MLflow,
- sauvegarder le modèle.

## 3. Backend

Le backend est développé avec **FastAPI**.

Il expose :

- une route de santé `/health`,
- une route `/predict` pour faire une prédiction.

## 4. Frontend

Le frontend est développé avec **Streamlit**.

Il permet à l’utilisateur de saisir les 4 valeurs et d’obtenir la prédiction du modèle.

## 5. Tests

Des tests simples permettent de vérifier :

- que l’API répond,
- que la route de prédiction fonctionne.

## 6. Docker

Le backend et le frontend sont conteneurisés séparément.

Un fichier `docker-compose.yml` permet de les lancer ensemble.

## 7. CI/CD

Le pipeline GitHub Actions a pour rôle de :

- lancer les tests,
- construire les images Docker,
- pousser les images sur Docker Hub,
- préparer le déploiement sur Azure.

## 8. Déploiement

Le déploiement final se fait sur Azure à partir des images construites par le pipeline.
