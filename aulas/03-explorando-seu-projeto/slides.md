---
marp: true
title: Explorando seu projeto
---

Desenvolvimento Aberto
===

# ![width:300px](../02-contribuicao-de-codigo/capa.svg)

##### Explorando seu projeto 


###### Igor dos Santos Montagner ( [igorsm1@insper.edu.br](mailto:igorsm1@insper.edu.br) )

---

# Aulas passadas

* Workflow para projetos distribuídos
* Escolher projeto e issue para primeira contribuição
	- Registre a issue escolhida em [insper/dev-aberto/issues/45](https://github.com/Insper/dev-aberto/issues/45)

---

# Pandas (Issues)

### Formatação

* [[1]](https://github.com/pandas-dev/pandas/issues/27563), [[2]](https://github.com/pandas-dev/pandas/issues/13257), [[3]](https://github.com/pandas-dev/pandas/issues/25955)

### Pré-processamento

* [[1]](https://github.com/pandas-dev/pandas/issues/13628), [[2]](https://github.com/pandas-dev/pandas/issues/18198), [[3]](https://github.com/pandas-dev/pandas/issues/16698)

### Entrada/saída:

* [[1]](https://github.com/pandas-dev/pandas/issues/26692), [[2]](https://github.com/pandas-dev/pandas/issues/22853)

### Visualização

* [[1]](https://github.com/pandas-dev/pandas/issues/14119)

---

# Sphinx

Projeto para documentação de projetos. Usado para documentar o próprio Python.

* Trabalha com textos em diversos formatos
* Faz referência entre documentos e com código fonte.

### Exemplos

* [[1]](https://github.com/sphinx-doc/sphinx/issues/4731) 

### Documentos e formatação

* [[1]](https://github.com/sphinx-doc/sphinx/issues/6241) [[2]](https://github.com/sphinx-doc/sphinx/issues/6094) [[3]](https://github.com/sphinx-doc/sphinx/issues/4925)


---

# "Regras" para debugar qualquer coisa
## Ferramentas para compilar e se achar em um projeto
---

# 9 regras de debug

![](livro.jpg)

---

# 9 regras de debug

1. UNDERSTAND THE SYSTEM
1. MAKE IT FAIL
1. QUIT THINKING AND LOOK
1. DIVIDE AND CONQUER
1. CHANGE ONE THING AT A TIME
1. KEEP AN AUDIT TRAIL
1. CHECK THE P LUG
1. GET A FRESH VIEW
1. IF YOU DIDN'T FIX IT, IT AIN'T FIXED

----

# 1. Understand the system

## Nada acontece se não conseguirmos

1. Baixar a versão de desenvolvimento
2. Instalar todas as dependências
3. Compilar nossa própria versão
4. Rodar testes na versão do `master`

---

# 1. Understand the system

## Ferramentas importantes:

1. [Virtual environments](https://realpython.com/python-virtual-environments-a-primer/): venv, virtualenv, pipenv, conda
1. [setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode) - *development mode*
1. Debugging
	- *pdb*
	- função `breakpoint()` ([tutorial](https://hackernoon.com/python-3-7s-new-builtin-breakpoint-a-quick-tour-4f1aebc444c))

----

# 2. Make it fail

## Reproduza seu bug

* Crie um exemplo mínimo que reproduza o bug desejado ou que usaria a feature que quer implementar
	- entrada de exemplo e saída esperada vs saída obtida
* Possivelmente isto já foi descrito na *issue* escolhida.

---

# 3. Quit thinking and look

## Encontre onde está o problema e leia o código com atenção

1. Encontre no código onde o bug pode estar
2. Comece geral (em qual arquivo está a funcionalidade?) e vá restringindo (em qual função o bug "explode"?)
3. Ferramentas de debug são essenciais. Veja o item 1.
	- Não atenderei ninguém que esteja debugando só com `print`

----

# 3. Quit thinking and look

## Buscando por nomes de arquivos

Comando `find` ([man page](http://man7.org/linux/man-pages/man1/find.1.html))

**Exemplo**: procurar por arquivos cujo nome é aceito por uma certa expressão regular começando no diretório atual.

> `$ find -iname "regexp" .`

---

# 3. Quit thinking and look

## Buscando no conteúdo dos arquivos

Comando `egrep` ([man page](https://linux.die.net/man/1/egrep))

> `$ egrep [OPTIONS] PATTERN FILES`

* `PATTERN`: expressão regular
* `FILES`: lista de diretórios ou arquivos

---

# 3. Quit thinking and look - grep

**Exemplo 1**: buscar todos arquivos nas pasta atual (.) e subpastas com o texto "dialog" ignorando maiúsculas/minúsculas.

> `$ grep -r -i dialog .`

#

**Exemplo 2**: Listas todos os arquivos *.cpp* que fazem algum include

> `$ grep -r --include "*cpp" "#include" .`


----

# 4. Divide and Conquer

## Crie um plano de ação

1. Por que o bug ocorre? 
	- Está relacionado a qual função? 
	- Qual variável tem o valor errado?
2. O que deve ser mudado para que pare de ocorrer?


**Pré-requisito**: escolhar uma linha da função que dá pau e colocar um `breakpoint()`

----

# 5. Change one thing at a time

## Um bom PR muda o mínimo possível

* use várias branches se quiser testar ideias diferentes


----

# 6. KEEP AN AUDIT TRAIL

## Registre suas descobertas

- Log de como você encontrou onde mexer
- Log de todos arquivos de interesse e seus usos
- Log de todas as pesquisas feitas
- Log de todas as modificações feitas


**Não se esqueça**:`git diff` é seu melhor amigo

---

# 7. Check the plug

## Nunca se esqueça de testar a soluções mais simples primeiro


---

# 8. GET A FRESH VIEW

## Empacou?

É por isso que vocês trabalham em grupo no primeiro bug. 

## Empacou mesmo?

Para isto serve seu grupo. 

## Empacou mesmo!?!?!?!?

Me chame!

---

# 9. IF YOU DIDN'T FIX IT, IT AIN'T FIXED

![](doesnt-work.png)


---

# Hora de programar

----

Desenvolvimento Aberto
===

# ![width:300px](../02-contribuicao-de-codigo/capa.svg)

##### Explorando seu projeto 


###### Igor dos Santos Montagner ( [igorsm1@insper.edu.br](mailto:igorsm1@insper.edu.br) )
