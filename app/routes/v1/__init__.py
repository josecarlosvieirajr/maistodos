"""
# Routes

## V1: API inicial

Attributes:
    api_router: Router da API v1.

Args:
    router_credit_card: Rota de cartão de crédito.
    router_health: Rota de health check.
"""
from fastapi import APIRouter

from app.views import router_auth, router_credit_card, router_health

api_router = APIRouter()

api_router.include_router(
    router_health,
    prefix="/v1/health",
    tags=["health"],
)

api_router.include_router(
    router_credit_card,
    prefix="/v1/credit-card",
    tags=["credit-card"],
)

api_router.include_router(
    router_auth,
    prefix="/v1/auth",
    tags=["auth"],
)
