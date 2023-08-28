---
marp: true
title: Documentação de API e linters
footer: 'Igor Montagner ![License CC BY-NC-SA 4.0](../cc-by-nc-sa.png)'
---

<style>
	footer {
		position: fixed;
		bottom: 10px;
		left: 1050px;
		width: 400px;
	}

	footer img {
		vertical-align: middle;
	}
</style>


Desenvolvimento Aberto
===

![100%](capa.svg)

##### Documentação de API e linters

###### Igor dos Santos Montagner ( [igorsm1@insper.edu.br](mailto:igorsm1@insper.edu.br) )

----

# Discussão: o que faz o projeto?

---

# Servidor de desafios

Vocês rodaram um MVP do servidor de desafios. Veja abaixo seu estado atual:

https://github.com/Insper/servidor-de-desafios

----

# Servidor de desafios

![](foto-dessoft.png)

----

# Discussão: como o projeto está organizado? (tecnologias)

----


# Discussão: como o projeto está organizado? (código)

----

# Discussão: avalie a arquitetura do projeto 

## 0 a 10

----

# Discussão: avalie a qualidade de código do projeto. 

## 0 a 10

----

# Discussão: avalie a segurança do projeto. 

## 0 a 10

----

# Discussão: esse projeto é um projeto "profissional"?

## 0 a 10

----

# Discussão: o que você incluiria na documentação do projeto?

----

## Software tem história e depende de pessoas para evoluir

---

# Código *vs* software profissional

Os seguintes pontos transformam um código que fiz para mim em algo útil para outras pessoas

1. Traduções e internacionalização (datas)
2. Documentação de usuário e de desenvolvimento
3. Algum processo de qualidade de software
	- testes automatizados
	- formatação de código e estrutura de repo
4. pacotes de instalação

---
# Hoje

- Ferramentas de documentação
- Documentação de API usando
- Padrões de formatação de código
	- linters
	- PEP8

---
# Documentação de API

**Objetivo**: explicar o funcionamento das funções, classes e módulos de um programa. 

- Focado em detalhes
- Documenta os argumentos esperados e em quais situações a função funciona 
- Tipicamente obtida direto do código
- Não detalha como as funções são usadas em conjunto

---
# Documentação de API

![center](api-doc.svg)

---
# Documentação de API

![2000% center](np-doc-api.png)

[ref](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html)

---
# Ferramentas

- Python:
	- pydoc, numpydoc
- C/C++
	- Doxygen
- Java
	- Javadoc

Em geral podem ser plugadas em alguma ferramenta de documentação de projetos. 

---
# Padrões de codificação

![width:500px](porco.png)

---
# Padrões de codificação

![width:900px](porco-pylint.png)

---
# Padrões de codificação

- Cada projeto tem o seu
- Algumas linguagens tem um estilo padrão
	- Python - PEP8
- Ferramentas ajudam a conferir (forçar) um estilo específico

---
# Ferramentas

- Python: pylint, black
- C/C++: splint, cppchecker, gcc (opções -Wall, -Wextra), clang-format/-tidy
- Java: flag `-Xlint`
- Javascript: ESlint, TSlint (typescript)

#

Ajudam a manter código limpo e legível. Podem ser plugadas no seu editor favorito.

## Execução obrigatória para muitos projetos grandes

----

# Atividade prática: Projeto profissional

![width:256px](star.svg)


**Objetivo**: Transformar um código perdido em um projeto 

> "metadata": {"url": "github pages criado", "group": ["ate três", "alunos"]}

---


Desenvolvimento Aberto
===

![100%](capa.svg)

##### Documentação de API + testes


###### Igor dos Santos Montagner ( [igorsm1@insper.edu.br](mailto:igorsm1@insper.edu.br) )


