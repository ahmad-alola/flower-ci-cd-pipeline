# API

## Présentation

L’API a été développée avec **FastAPI**.

Elle permet d’utiliser le modèle entraîné pour faire des prédictions.

## Route `/health`

### Méthode

`GET /health`

### Rôle

Cette route permet de vérifier que l’API fonctionne.

### Réponse attendue

```json
{
  "status": "ok"
}
```

---

## Route `/predict`

### Méthode

`POST /predict`

### Rôle

Cette route reçoit les caractéristiques d’une fleur et retourne la classe prédite.

### Exemple de requête

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Exemple de réponse

```json
{
  "prediction": "setosa"
}
```

---

## Lancement local de l’API

Depuis le dossier `backend` :

```bash
uvicorn app.main:app --reload
```

Puis ouvrir :

```text
http://127.0.0.1:8000/docs
```

Cette page permet de tester directement les routes avec Swagger UI.
