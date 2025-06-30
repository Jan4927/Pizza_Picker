from app import app

def test_pick_returns_pizza():
    client = app.test_client()
    resp = client.post("/pick", json={})
    assert resp.status_code == 200

def test_pick_vegetarian():
    client = app.test_client()
    resp = client.post("/pick", json={"vegetarian": True})
    data = resp.get_json()
    assert data["vegetarian"] is True
