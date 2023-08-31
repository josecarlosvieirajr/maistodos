## Decisões Tecnicas

Ao desenvolver o projeto Python utilizando o FastAPI, foram tomadas decisões técnicas cuidadosamente selecionadas para garantir a qualidade, desempenho e segurança da aplicação. Abaixo estão as decisões tomadas e as respectivas justificativas técnicas para cada uma delas:

## [Python](https://www.python.org/downloads/release/python-31013/) = "^3.10"

A escolha da versão Python 3.10 como requisito mínimo é baseada na busca por aproveitar os recursos e melhorias mais recentes da linguagem. A versão 3.10 traz otimizações de desempenho, novas funcionalidades e melhorias de sintaxe que podem contribuir para um código mais limpo e eficiente.

Não optando por usar a 3.11, pois durante o desenvolvimento deste projeto, ainda estar em fase de aperfeiçoamento.

## [FastAPI](https://fastapi.tiangolo.com/)

O FastAPI é uma estrutura moderna e de alto desempenho para construção de APIs web em Python. A escolha se baseia na busca por aproveitar as atualizações recentes da biblioteca, que podem trazer melhorias de desempenho, correções de bugs e novos recursos. A adoção do FastAPI permite o desenvolvimento rápido de APIs assíncronas, garantindo uma ótima experiência tanto para os desenvolvedores quanto para os usuários da API.

Alem de possuir integração nativa com o swagger, ser open-source com uma comunidade muito ativa e possuir uma otima documentação

## [SQLModel](https://sqlmodel.tiangolo.com/)

O SQLModel é uma biblioteca que oferece suporte a operações de banco de dados utilizando SQLAlchemy com tipagem de dados Pydantic. A escolha se deu pela facilidade na integração com o fastapi, e também, pensando no potencial para se beneficiar de melhorias futuras. A utilização do SQLModel facilita a definição de modelos de dados de forma declarativa e a interação com o banco de dados de maneira eficiente e segura.

O SQLModel é um ORM bastante recente, porem tem o criador do fastapi como seu desenvolvedor principal, por isso, esse projeto é open-source e herda a comunidade do fastapi na sua manutenção

!!! warning "SQLModel"
    Esse ORM foi utilizado nesse projeto, apenas por ser uma base de teste tecnico, o SQLModel apesar de ser muito simples e facil de implementar, ainda está em fase de desenvolvimento.
    
    por tanto, esse projeto **NÃO DEVE SER UTILIZADO EM PRODUÇÃO** nesse moldes.

## [Python-Jose](https://github.com/mpdavis/python-jose)

O Python-Jose é uma biblioteca para manipulação de tokens JWT (JSON Web Tokens) em Python. A inclusão da dependência "cryptography" se dá pelo fato de ser uma biblioteca amplamente reconhecida para operações criptográficas. A utilização de tokens JWT é uma prática comum para autenticação e autorização em APIs, oferecendo segurança e escalabilidade.


___

Cada decisão técnica tomada foi fundamentada na busca por melhores práticas de desenvolvimento, desempenho e segurança. Essas escolhas contribuirão para a criação de uma aplicação confiável, eficiente e de fácil manutenção, oferecendo uma ótima experiência tanto para os desenvolvedores quanto para os usuários finais.

Todas as decisões aqui detalhadas são baseadas na criatividade do dev [:fontawesome-brands-github:]({{ git.my }})