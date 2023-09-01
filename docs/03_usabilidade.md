## Testando a API.

A melhor forma de testar a api, depois de inicia-la, é usando pelo próprio swagger, lá temos a descrição de todas as rotas e de como usar.

### Passo 1:
- Acesse a url do swagger no seu browser `http://localhost:8000/api/docs`
- Na rota `/api/v1/auth`, clique no botão [Try it out]. Após o click se abre o campo para edição
- No campo `Request body` coloque um username qualquer para gerar o token.
- Após preencher, clique em `Executar`

![](assets/step01.gif)


### Passo 2:
- Após o clique no Executar, no campo `Response Body`, terá um payload no padrão:
```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTY5MzUzNDUyMH0.fqm7YSpzGr0xuc9iIFyK3PURuaaLtwQfutBOx-ig_34",
  "token_type": "bearer"
}
```
- Copiando o conteudo que está na chave `access_token`, e colando no campo de token de qualquer uma das rotas.
![](assets/step02.gif)

## Expiração do Token

Esse mesmo token pode ser usado em todas as rotas do app por até `15min`, 
após esse tempo o token será rejeitado e será necessário gerar um novo token.