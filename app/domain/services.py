"""Camada de lógica de domínio do Uni-Bike."""

import sqlite3


class SystemHealthService:
    """Serviço de verificação operacional e acesso inicial à frota."""

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def get_system_status(self) -> dict[str, object]:
        """Verifica conectividade à base de dados e contabiliza e-bikes registadas."""
        row = self.conn.execute("SELECT COUNT(*) AS total FROM ebikes").fetchone()
        total_bikes = int(row["total"]) if row else 0
        return {"status": "ok", "database": "connected", "total_bikes": total_bikes}

    def list_bikes(self) -> list[dict[str, object]]:
        """Devolve a lista de e-bikes persistidas na base de dados."""
        rows = self.conn.execute(
            "SELECT id, qr_code, estado, bateria_pct, doca_id FROM ebikes ORDER BY id"
        ).fetchall()
        return [dict(row) for row in rows]
