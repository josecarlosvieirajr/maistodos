"""
## Initialize the FastAPI application.
Nesse modulo inicial é onde é criado o app FastAPI e adicionado os middlewares e rotas.

- Para acessar as informações de configuração, basta importar o módulo `config` e acessar o atributo `settings`.
- As rotas estão disponiveis no módulo `routes`.
"""


import logging
import logging.config

from fastapi import FastAPI
from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware

from app.config import settings
from app.db.model import engine
from app.routes import api_router_v1

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title=settings.service_name)

    SQLModel.metadata.create_all(engine)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router_v1, prefix="/api")

    logger.info(f"starting app {settings.service_name}")

    return app
