"""
## Módulo de Utilitarios.
Itens que podem ser reutilizados em outros módulos do projeto

Functions:
    hashable: Gera o hash SHA-256 de um valor.
    datetime_validator: Valida e formata uma data no formato mês/ano.
"""
import hashlib
from datetime import datetime, timedelta


def hashable(value):
    """
    Gera o hash SHA-256 de um valor.

    Esta função calcula o hash SHA-256 de um valor dado usando a biblioteca hashlib do Python.

    Args:
        value (str): O valor a ser hasheado.

    Returns:
        value (str): O hash SHA-256 em formato hexadecimal.

    Example:
        original_text = "senha123"
        hashed_value = hashable(original_text)
        print(f"O valor hasheado é: {hashed_value}")
    """
    hash_object = hashlib.sha256()
    hash_object.update(value.encode())
    return hash_object.hexdigest()


def datetime_validator(value: str) -> str:
    """
    Valida e formata uma data no formato mês/ano.

    Esta função recebe uma data no formato "mês/ano" e realiza as seguintes operações:
    - Valida se a data é posterior à data atual.
    - Calcula e retorna o último dia do mês correspondente à data fornecida, no formato "ano-mês-dia".

    Args:
        value (str): A data no formato "mês/ano" a ser validada e formatada.

    Returns:
        value (str): O último dia do mês correspondente à data, no formato "ano-mês-dia".

    Raises:
        ValueError: Se a data fornecida não for posterior à data atual.

    Example:
        input_date = "08/2023"
        formatted_date = datetime_validator(input_date)
        print(f"Último dia do mês: {formatted_date}")
    """
    input_format = "%m/%Y"
    output_format = "%Y-%m-%d"
    today = datetime.now().date()

    parsed_date = datetime.strptime(value, input_format).date()
    last_day_of_month = (parsed_date.replace(day=1) + timedelta(days=32)).replace(
        day=1
    ) - timedelta(days=1)

    if last_day_of_month < today:
        raise ValueError("The input date is not earlier than today.")

    return last_day_of_month.strftime(output_format)
