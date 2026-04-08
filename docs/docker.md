# Docker

## Objectif

L’objectif de Docker dans ce projet est de rendre le backend et le frontend faciles à lancer, à transporter et à déployer.

## Conteneurs utilisés

Le projet contient deux conteneurs :

- un conteneur pour le **backend FastAPI**,
- un conteneur pour le **frontend Streamlit**.

## Lancement avec Docker Compose

Depuis la racine du projet :

```bash
docker compose up --build
```

## Services exposés

- Backend : `http://localhost:8000/docs`
- Frontend : `http://localhost:8501`

## Avantages

L’utilisation de Docker permet :

- d’avoir le même environnement partout,
- d’éviter les problèmes d’installation locale,
- de préparer plus facilement le déploiement sur Azure,
- d’intégrer la construction des images dans le pipeline CI/CD.
