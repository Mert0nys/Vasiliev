import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Тест1", "description": "Вымыть пол", "status": "created"})
    assert response.status_code == 200  
    assert response.json()["title"] == "Тест1"

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  

def test_update_task():
    create_response = client.post("/tasks/", json={"title": "Тест1", "description": "Вымыть пол", "status": "created"})
    task_id = create_response.json()["id"]  
    response = client.put(f"/tasks/{task_id}", json={"title": "Тест2", "description": "Вымыть посуду", "status": "in_progress"})
    assert response.status_code == 200
    assert response.json()["title"] == "Тест2"  

def test_delete_task():
    
    create_response = client.post("/tasks/", json={"title": "Тест1", "description": "Вымыть пол", "status": "created"})
    task_id = create_response.json()["id"]  
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
