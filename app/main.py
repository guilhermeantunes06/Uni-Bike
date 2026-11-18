"""Ponto de entrada da aplicação FastAPI Uni-Bike."""

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes import router as api_router
from app.infrastructure.database import init_db, seed_initial_data

STATIC_DIR = Path(__file__).resolve().parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Inicializa a base de dados e os dados base ao arrancar a aplicação."""
    init_db()
    seed_initial_data()
    yield


app = FastAPI(
    title="Uni-Bike API",
    version="0.1.0",
    description="Interface de serviços REST do sistema Uni-Bike (1.º Incremento).",
    lifespan=lifespan,
)

app.include_router(api_router)
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/", include_in_schema=False)
def serve_frontend() -> FileResponse:
    """Serve a aplicação web inicial (testável com Playwright)."""
    return FileResponse(STATIC_DIR / "index.html")
