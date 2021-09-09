# 08 - Testes automatizados

O objetivo da atividade de hoje é criar testes automatizados para o servidor de desafios. Com isso completamos nossa jornada rumo a software que possa ser desenvolvido de maneira colaborativa e que possa ser usado em situações reais. 

1. Documentação (usuários e desenvolvedor)
2. Distribuição de software e versionamento 
3. Localização e internacionalização
4. Testes automatizados

## Testes de unidade

Uma parte do programa do servidor de desafios que pode ser testada com testes de unidade é a função `lambda_handler`, que executa a função submetida pelo usuário. Seu trabalho será criar testes usando o [pytest](https://docs.pytest.org/en/latest/contents.html#toc) e cobrir  os seguintes casos:

- [ ] programa submetido está correto
- [ ] programa submetido não contém a função pedida
- [ ] programa submetido retorna resultado incorreto

## Testes de interface de usuário

Iremos criar testes de interface de usuário para o Servidor de Desafios usando o [*Selenium*](https://selenium-python.readthedocs.io/). Este software permite imitar interações reais de um usuário usando código e criar testes baseado nessas interações. 

Vocês devem simular os seguintes cenários:

- [ ] Aluno faz login com sucesso
- [ ] Aluno entra senha incorreta
- [ ] Aluno envia desafio com resposta incorreta
- [ ] Aluno envia desafio com resposta correta

A ideia básica seria reproduzir os mesmos testes apresentados no manual do usuário.

## Entrega

Coloquem os scripts de teste na pasta *test* do repositório e adicionem instruções de como rodar os testes no `README`.
