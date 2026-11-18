"""Testes do esqueleto inicial da aplicação (Walking Skeleton)."""

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> TestClient:
    """Cria um cliente HTTP de teste com base de dados SQLite isolada por execução."""
    db_file = tmp_path / "test_unibike.db"
    monkeypatch.setenv("UNIBIKE_DB_PATH", str(db_file))
    with TestClient(app) as test_client:
        yield test_client


def test_health_endpoint_traverses_all_layers(client: TestClient) -> None:
    """Verifica que GET /api/health atravessa API -> Domínio -> SQLite."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["database"] == "connected"
    assert data["total_bikes"] >= 1


def test_list_bikes_returns_seeded_fleet(client: TestClient) -> None:
    """Verifica que GET /api/ebikes devolve a bicicleta inicial persistida em SQLite."""
    response = client.get("/api/ebikes")
    assert response.status_code == 200
    bikes = response.json()
    assert len(bikes) == 1
    assert bikes[0]["id"] == "BIKE-001"
    assert bikes[0]["qr_code"] == "QR-BIKE-001"
    assert bikes[0]["estado"] == "Disponivel"


def test_web_ui_is_served(client: TestClient) -> None:
    """Verifica que a página web principal é servida com seletores estáveis para Playwright."""
    response = client.get("/")
    assert response.status_code == 200
    assert 'data-testid="app-title"' in response.text
    assert 'data-testid="bikes-list"' in response.text
