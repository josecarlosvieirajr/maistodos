FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install poetry
RUN poetry install

EXPOSE 8001

CMD ["poetry", "run", "uvicorn", "asgi:application", "--host", "0.0.0.0", "--port", "8001"]

