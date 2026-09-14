import pytest
from app.main import app, add_numbers

@pytest.fixture
def client():
    """Configure le client de test Flask."""
    with app.test_client() as client:
        yield client

def test_add_logic():
    """Test unitaire de la fonction de calcul."""
    assert add_numbers(10, 5) == 15
    assert add_numbers(-1, 1) == 0

def test_home_route(client):
    """Test d'intégration de la route d'accueil."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bienvenue" in response.data

def test_api_add_route(client):
    """Test de l'API JSON."""
    response = client.get('/api/add/5/5')
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 10
