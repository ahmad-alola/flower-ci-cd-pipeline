from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={
        "sepal_length": 5.0,
        "sepal_width": 2.0,
        "petal_length": 3.5,
        "petal_width": 1.0
    })

    print(response.json())

    assert response.status_code == 200
    assert "prediction" in response.json()
    
