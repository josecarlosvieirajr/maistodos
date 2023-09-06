"""
# Modulo de Excessões
Item usado para disponibilizar as excessões personalizadas da aplicação.
"""

from crud_error import CRUDCreateError, CRUDUpdateError, CRUDDeleteError, CRUDSelectError
from http_error_schema import HTTPError

__all__ = [
    "CRUDCreateError",
    "CRUDUpdateError",
    "CRUDDeleteError",
    "CRUDSelectError",
    "HTTPError",
]
