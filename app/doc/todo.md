# Itens que estão faltando no projeto


- [x] Criar as classes de erro
- [x] Adicionar docstrings as novas classes
- [x] refatorar o codigo para aceitar as novas classes
- [x] refatorar os testes para validar esses erros e seus textos

_nesse passo deve-se usar `pytest.raises` ignorando o regex_
```
 with pytest.raises(CRUDUpdateError, match=re.escape(msg_error)):
```
- [ ] escrever um bloco na documentacao sobre as classes de erros
- [ ] rebuild da doc no readthedocs