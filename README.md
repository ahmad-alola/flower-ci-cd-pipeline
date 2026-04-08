# flower-ci-cd-pipeline

Projet simple de mise en place d’un pipeline CI/CD autour d’une application de machine learning.

## Objectif du projet

Ce projet a pour objectif de montrer un workflow complet, de l’entraînement d’un modèle jusqu’au déploiement :

- préparation et chargement des données,
- entraînement d’un modèle de classification Iris,
- suivi de l’entraînement avec MLflow,
- mise à disposition du modèle via une API FastAPI,
- création d’une interface simple avec Streamlit,
- conteneurisation avec Docker,
- automatisation avec GitHub Actions,
- déploiement sur Azure.

Le but n’est pas de créer un modèle complexe, mais de comprendre et mettre en place toutes les étapes d’un pipeline CI/CD simple et fonctionnel.

---

## Structure du projet

```text
flower-ci-cd-pipeline/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── schemas.py
│   ├── models/
│   │   └── iris_model.joblib
│   ├── tests/
│   │   ├── test_health.py
│   │   └── test_predict.py
│   ├── train.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── pytest.ini
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── notebooks/
│   └── 01_iris_analysis_training.ipynb
├── data/
│   └── iris.csv
├── docs/
│   ├── index.md
│   ├── architecture.md
│   ├── api.md
│   ├── docker.md
│   └── deployment.md
├── docker-compose.yml
├── mkdocs.yml
├── .gitignore
└── README.md
```

---

## Technologies utilisées

- **Python**
- **scikit-learn**
- **pandas**
- **MLflow**
- **FastAPI**
- **Streamlit**
- **pytest**
- **Docker / Docker Compose**
- **GitHub Actions**
- **Azure**
- **MkDocs**

---

## Jeu de données

Le projet utilise le dataset **Iris**.

Deux approches ont été utilisées :

1. chargement direct du dataset depuis `scikit-learn`,
2. export du dataset dans un fichier CSV pour pouvoir l’analyser plus facilement dans un notebook.

Ce choix permet de garder un projet simple, tout en montrant une logique proche d’un vrai projet de data.

---

## Entraînement du modèle

Le modèle est entraîné dans le fichier :

```bash
backend/train.py
```

Étapes principales :

- chargement des données,
- suppression des doublons et des valeurs manquantes,
- séparation train / test,
- entraînement d’un `RandomForestClassifier`,
- calcul de l’accuracy,
- suivi de l’expérience avec MLflow,
- sauvegarde du modèle dans `backend/models/iris_model.joblib`.

---

## Lancer le projet en local

### 1. Activer l’environnement virtuel

```bash
source venv/bin/activate
```

### 2. Installer les dépendances du backend

```bash
cd backend
pip install -r requirements.txt
```

### 3. Entraîner le modèle

```bash
python train.py
```

### 4. Lancer l’API

```bash
uvicorn app.main:app --reload
```

### 5. Lancer le frontend

Dans un autre terminal :

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## Tests

Les tests sont dans :

```text
backend/tests/
```

Pour les lancer :

```bash
cd backend
pytest
```

---

## Docker

Pour lancer les deux services avec Docker :

```bash
docker compose up --build
```

Services disponibles :

- Backend : `http://localhost:8000/docs`
- Frontend : `http://localhost:8501`

---

## CI/CD

Le pipeline CI/CD doit :

- se lancer à chaque push sur `main`,
- exécuter les tests,
- construire les images Docker du backend et du frontend,
- pousser les images sur Docker Hub,
- permettre le redéploiement des applications sur Azure.

---

## Documentation

La documentation du projet est générée avec **MkDocs**.

Pour la lancer localement :

```bash
mkdocs serve
```

Pour générer le site statique :

```bash
mkdocs build
```

---

## Livrables attendus

- lien du dépôt GitHub,
- lien des applications déployées sur Azure,
- pipeline CI/CD fonctionnel,
- code propre et compréhensible.

---

## Auteur

Projet réalisé dans le cadre d’un exercice de mise en place d’un pipeline CI/CD.
