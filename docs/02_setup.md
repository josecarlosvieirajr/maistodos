## Instalação e Execução do Projeto

Neste guia, apresentaremos duas opções para instalar e executar o projeto Python usando FastAPI. Você pode escolher entre as opções de instalação via Poetry ou Docker, ambas projetadas para simplificar o processo de configuração e execução.

## Opção 1: Instalação e Execução via Poetry

**Passo 1: Pré-requisitos**
Certifique-se de que você tenha o Python e o Poetry instalados em seu sistema. Caso contrário, você pode instalá-los seguindo as instruções em:

- Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Poetry: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

**Passo 2: Clonando o Repositório**
Clone o repositório do projeto para o seu ambiente local:
```bash
git clone https://github.com/josecarlosvieirajr/maistodos
cd maistodos
```

**Passo 3: Instalando Dependências**
Dentro da pasta raiz do projeto, execute o seguinte comando para instalar as dependências usando Poetry:
```bash
poetry install
```

**Passo 4: Executando o Projeto**
Após a instalação das dependências, execute o seguinte comando para iniciar o projeto:
```bash
task start
```
!!! warning "Atalho"
    Esse comando `task start`, é um atalho criado usando a lib [taskipy](https://github.com/taskipy/taskipy), caso tenha algum problema
    ao executar, inicie o projeto usando:
    `poetry run uvicorn asgi:application`

## Opção 2: Instalação e Execução via Docker

**Passo 1: Pré-requisitos**
Certifique-se de ter o Docker instalado em seu sistema. Se você ainda não o tiver, siga as instruções em: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

**Passo 2: Clonando o Repositório**
Clone o repositório do projeto para o seu ambiente local:
```bash
git clone https://github.com/josecarlosvieirajr/maistodos
cd maistodos
```

**Passo 3: Construindo e Iniciando o Contêiner Docker**
Dentro da pasta raiz do projeto, execute o seguinte comando para construir e iniciar o contêiner Docker:
```bash
docker-compose build && docker-compose up -d
```

Após a execução deste comando, o projeto estará em execução dentro de um contêiner Docker.

## Acessando a Aplicação

Depois de seguir um dos métodos de instalação acima, você poderá acessar a aplicação através do navegador. Acesse a seguinte URL:
```
http://localhost:8000
```

Isso abrirá a documentação do projeto.

## Acessando o Swagger Aplicação

Para acessar o swagger onde é possivel você interajir com os endpoints e testar as funcionalidades do projeto. Acesse:
```
http://localhost:8000/api/docs
```

## Encerrando a Execução

### Docker
Se você estiver usando a opção Docker, para encerrar a execução do projeto, execute o seguinte comando na pasta raiz do projeto:
```bash
docker-compose down
```

### Poetry
Se você estiver usando a opção Poetry, para encerrar a execução do projeto, basta encerrar o processo no terminal.

___

Esperamos que este guia tenha sido útil para instalar e executar o projeto usando o FastAPI. Se você tiver alguma dúvida ou encontrar problemas durante o processo, não hesite em entrar em contato com a equipe de suporte.

Aproveite a experiência de desenvolvimento com o FastAPI e explore todas as funcionalidades oferecidas pelo projeto!