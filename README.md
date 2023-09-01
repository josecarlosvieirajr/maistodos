# MAISTODOS

[![Documentation Status](https://readthedocs.org/projects/maistodos/badge/?version=latest)](https://maistodos.readthedocs.io/pt/latest/?badge=latest)
[![CI](https://github.com/josecarlosvieirajr/maistodos/actions/workflows/ci.yml/badge.svg)](https://github.com/josecarlosvieirajr/maistodos/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/josecarlosvieirajr/maistodos/graph/badge.svg?token=KAMFN9ZLCD)](https://codecov.io/gh/josecarlosvieirajr/maistodos)

## Documentação da API de Cadastro de Cartões de Crédito

Bem-vindo à documentação da API de Cadastro de Cartões de Crédito da MAISTODOS LTDA! Neste guia, você encontrará informações abrangentes sobre como utilizar e integrar-se com o sistema inovador de cadastros de cartões de crédito. Este sistema foi projetado para garantir a qualidade, segurança e padronização dos dados, proporcionando uma experiência eficiente e confiável tanto para os usuários quanto para os desenvolvedores.

Nossa API de cadastro de cartões de crédito foi concebida como uma solução simples e robusta construida em Python, pronta para lidar com o processo de registro de cartões, atendendo às demandas do mercado em constante evolução. 

## **Acesse a Documentação completa aqui [readthedocs](https://maistodos.readthedocs.io/pt/latest/)**

## Diagrama - Fluxo dos dados na app

```mermaid
graph LR
    A1[Client] --> A[Route]
    A <--> B[GET];
    A <--> C[GET <\key>];
    A <--> D[POST];
    A <--> E[PUT];
    A <--> F[DELETE];
    B <--> G[View]
    C <--> G[View]
    D <--> G[View]
    E <--> G[View]
    F <--> G[View]
    G[View] <--> H{Repository}
    H <--> |OK| I(DB)
    H --> |Error| J[HTTPException]
    J ----> A1
```

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

## Testando a API.

A melhor forma de testar a api, depois de inicia-la, é usando pelo próprio swagger, lá temos a descrição de todas as rotas e de como usar.

### Passo 1:
- Acesse a url do swagger no seu browser `http://localhost:8000/api/docs`
- Na rota `/api/v1/auth`, clique no botão [Try it out]. Após o click se abre o campo para edição
- No campo `Request body` coloque um username qualquer para gerar o token.
- Após preencher, clique em `Executar`

![](docs/assets/step01.gif)


### Passo 2:
- Após o clique no Executar, no campo `Response Body`, terá um payload no padrão:
```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTY5MzUzNDUyMH0.fqm7YSpzGr0xuc9iIFyK3PURuaaLtwQfutBOx-ig_34",
  "token_type": "bearer"
}
```
- Copiando o conteudo que está na chave `access_token`, e colando no campo de token de qualquer uma das rotas.
![](docs/assets/step02.gif)

## Expiração do Token

Esse mesmo token pode ser usado em todas as rotas do app por até `15min`, 
após esse tempo o token será rejeitado e será necessário gerar um novo token.

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
