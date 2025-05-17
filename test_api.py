import pytest
from fastapi.testclient import TestClient
from main import app  # Importing FastAPI app from your main script

client = TestClient(app)

# Positive Test Case: Valid Topic & Proficiency Level
def test_generate_learning_pathway_success():
    response = client.get("/generate_learning_pathway/", params={"topic": "Artificial Intelligence", "proficiency_level": "Beginner"})
    assert response.status_code == 200  # Ensure response is OK
    assert "learning_pathway" in response.json()  # Ensure response contains expected key
    assert isinstance(response.json()["learning_pathway"], str)  # Ensure the output is a string

# Negative Test Case: Missing Parameters
def test_generate_learning_pathway_missing_params():
    response = client.get("/generate_learning_pathway/")
    print("response code :",response.status_code)
    assert response.status_code == 422  # FastAPI returns 422 for missing parameters

# Negative Test Case: Invalid Topic
def test_generate_learning_pathway_invalid_topic():
    response = client.get("/generate_learning_pathway/", params={"topic": "", "proficiency_level": "Beginner"})
    assert response.status_code == 200  # Ensure API handles empty topics gracefully
    assert "learning_pathway" in response.json()
    assert response.json()["learning_pathway"] != ""  # Check that pathway isn't empty



