"""Camada de interface de serviços (endpoints API REST)."""

import sqlite3
from fastapi import APIRouter, Depends

from app.domain.services import SystemHealthService
from app.infrastructure.database import get_db

router = APIRouter(prefix="/api", tags=["Sistema & Frota"])


@router.get("/health")
def health_check(conn: sqlite3.Connection = Depends(get_db)) -> dict[str, object]:
    """Endpoint de saúde que atravessa API -> Domínio -> Persistência SQLite."""
    service = SystemHealthService(conn)
    return service.get_system_status()


@router.get("/ebikes")
def list_bikes(conn: sqlite3.Connection = Depends(get_db)) -> list[dict[str, object]]:
    """Lista todas as e-bikes registadas na frota."""
    service = SystemHealthService(conn)
    return service.list_bikes()
