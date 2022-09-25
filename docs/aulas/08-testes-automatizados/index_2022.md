# 08 - Testes automatizados

O objetivo da atividade de hoje é criar testes automatizados para um projeto específico de software. Com isso completamos nossa jornada rumo a software que possa ser desenvolvido de maneira colaborativa e que possa ser usado em situações reais. 

1. Documentação (usuários e desenvolvedor)
2. Distribuição de software e versionamento 
3. Localização e internacionalização
4. Testes automatizados

## Biblioteca para implementação de agentes baseados em busca

O projeto [AI Code](https://github.com/Insper/ai_code) implementa uma biblioteca que possui diversos algoritmos de busca pré-prontos e alguns exemplos de utilização. 

Os exemplos de utilização já possuem arquivos de teste usando a biblioteca `pytest`, mas podem estar incompletos ou até mesmo errados. 

As implementações dos algoritmos de busca, da biblioteca em si, não possuem testes. Estes algoritmos estão implementados no arquivo `SearchAlgoritms.py`. 

## Atividades

* Faça um fork do projeto; 
* Leia a documentação para entender os exemplos e o propósito da biblioteca; 
* Revise os testes;
* Implemente ou altere 3 novos testes para um dos exemplos apresentados na documentação. Justifique o motivo da sua nova implementação ou alteração no *pull request*; 
* Implemente 3 novos testes para os algoritmos base da biblioteca. Faça isto em um *pull request* diferente do anterior. 

Além da implementação dos testes, uma outra alternativa é executar o `pylint` e sugerir mudanças na formatação do código dos arquivos `search/SearchAlgorithms.py`, `search/Graph.py` e `ProblemSpecificationExample.py`. 

## Formato de entrega

Para a entrega do exercício você deverá: 

* implementar os dois conjuntos de testes, ou;
* implementar um dos conjuntos de testes e as modificações sugeridas pelo `pylint`. 

Esta atividade deve ser individual. Os PRs devem ser enviados e discutidos ao longo desta semana. 