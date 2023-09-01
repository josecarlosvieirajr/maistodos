# Itens que estão faltando no projeto


- [ ] Criar as classes de erro
- [ ] Adicionar docstrings as novas classes
- [ ] refatorar o codigo para aceitar as novas classes
- [ ] refatorar os testes para validar esses erros e seus textos

_nesse passo deve-se usar `pytest.raises` ignorando o regex_
```
 with pytest.raises(CRUDUpdateError, match=re.escape(msg_error)):
```
- [ ] escrever um bloco na documentacao sobre as classes de erros