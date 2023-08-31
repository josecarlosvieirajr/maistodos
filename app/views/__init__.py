"""
Módulo de Visualizações (Views)
Este módulo é responsável por importar e disponibilizar as rotas (endpoints) para diferentes partes da aplicação.

As rotas importadas incluem:
- Rota de autenticação (router_auth)
- Rota de informações de cartão de crédito (router_credit_card)
- Rota de status da aplicação (router_health)
"""

from .auth import router as router_auth
from .credit_card import router as router_credit_card
from .health import router as router_health

__all__ = ["router_health", "router_credit_card", "router_auth"]
