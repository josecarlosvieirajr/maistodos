FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install poetry
RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]

