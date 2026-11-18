"""Persistência SQLite e gestão de esquema para o sistema Uni-Bike."""

import os
import sqlite3
from pathlib import Path
from typing import Iterator

DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent.parent / "unibike.db"


def get_db_path() -> str:
    """Devolve o caminho configurado para a base de dados SQLite."""
    return os.environ.get("UNIBIKE_DB_PATH", str(DEFAULT_DB_PATH))


def get_connection() -> sqlite3.Connection:
    """Abre uma ligação SQLite com row_factory configurado para acesso por nome de coluna."""
    conn = sqlite3.connect(get_db_path(), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db(conn: sqlite3.Connection | None = None) -> None:
    """Cria as tabelas base do modelo de domínio se ainda não existirem."""
    own_conn = conn is None
    if conn is None:
        conn = get_connection()

    try:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS organizacoes (
                id TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                dominio_email TEXT NOT NULL UNIQUE,
                contrato_ativo INTEGER NOT NULL DEFAULT 1
            );

            CREATE TABLE IF NOT EXISTS utilizadores (
                id TEXT PRIMARY KEY,
                email TEXT NOT NULL UNIQUE,
                nome TEXT NOT NULL,
                organizacao_id TEXT NOT NULL,
                ativo INTEGER NOT NULL DEFAULT 1,
                FOREIGN KEY (organizacao_id) REFERENCES organizacoes(id)
            );

            CREATE TABLE IF NOT EXISTS docas (
                id TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                raio_geofence_m REAL NOT NULL DEFAULT 15.0,
                capacidade INTEGER NOT NULL DEFAULT 10
            );

            CREATE TABLE IF NOT EXISTS ebikes (
                id TEXT PRIMARY KEY,
                qr_code TEXT NOT NULL UNIQUE,
                estado TEXT NOT NULL DEFAULT 'Disponivel',
                bateria_pct INTEGER NOT NULL DEFAULT 100,
                latitude REAL,
                longitude REAL,
                doca_id TEXT,
                ultimo_heartbeat TEXT,
                FOREIGN KEY (doca_id) REFERENCES docas(id)
            );

            CREATE TABLE IF NOT EXISTS viagens (
                id TEXT PRIMARY KEY,
                utilizador_id TEXT NOT NULL,
                ebike_id TEXT NOT NULL,
                doca_origem_id TEXT NOT NULL,
                doca_destino_id TEXT,
                estado TEXT NOT NULL DEFAULT 'EmCurso',
                distancia_km REAL NOT NULL DEFAULT 0.0,
                co2_poupado_kg REAL NOT NULL DEFAULT 0.0,
                inicio_ts TEXT NOT NULL,
                fim_ts TEXT,
                FOREIGN KEY (utilizador_id) REFERENCES utilizadores(id),
                FOREIGN KEY (ebike_id) REFERENCES ebikes(id),
                FOREIGN KEY (doca_origem_id) REFERENCES docas(id),
                FOREIGN KEY (doca_destino_id) REFERENCES docas(id)
            );

            CREATE TABLE IF NOT EXISTS metricas_esg (
                organizacao_id TEXT PRIMARY KEY,
                total_viagens INTEGER NOT NULL DEFAULT 0,
                total_km REAL NOT NULL DEFAULT 0.0,
                total_co2_poupado_kg REAL NOT NULL DEFAULT 0.0,
                FOREIGN KEY (organizacao_id) REFERENCES organizacoes(id)
            );
            """
        )
        conn.commit()
    finally:
        if own_conn:
            conn.close()


def seed_initial_data(conn: sqlite3.Connection | None = None) -> None:
    """Insere dados iniciais mínimos (organização, docas e e-bikes) de forma idempotente."""
    own_conn = conn is None
    if conn is None:
        conn = get_connection()

    try:
        conn.execute(
            """
            INSERT OR IGNORE INTO organizacoes (id, nome, dominio_email, contrato_ativo)
            VALUES ('ORG-UA', 'Universidade de Aveiro', 'ua.pt', 1);
            """
        )
        conn.execute(
            """
            INSERT OR IGNORE INTO docas (id, nome, latitude, longitude, raio_geofence_m, capacidade)
            VALUES ('DOCA-01', 'Reitoria UA', 40.6303, -8.6575, 15.0, 12);
            """
        )
        conn.execute(
            """
            INSERT OR IGNORE INTO ebikes (id, qr_code, estado, bateria_pct, latitude, longitude, doca_id)
            VALUES ('BIKE-001', 'QR-BIKE-001', 'Disponivel', 85, 40.6303, -8.6575, 'DOCA-01');
            """
        )
        conn.execute(
            """
            INSERT OR IGNORE INTO metricas_esg (organizacao_id, total_viagens, total_km, total_co2_poupado_kg)
            VALUES ('ORG-UA', 0, 0.0, 0.0);
            """
        )
        conn.commit()
    finally:
        if own_conn:
            conn.close()


def get_db() -> Iterator[sqlite3.Connection]:
    """Dependência FastAPI para obter e fechar a ligação SQLite por pedido."""
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()
