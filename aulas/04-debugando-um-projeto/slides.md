---
marp: true
title: Dicas de Debug
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

# ![height:350px](capa.svg)

##### Contribuição de código


###### Igor dos Santos Montagner ( [igorsm1@insper.edu.br](mailto:igorsm1@insper.edu.br) )

---

# Minha primeira contribuição de código

![width:256px](https://fonts.gstatic.com/s/i/materialicons/flight_takeoff/v6/24px.svg)

* Projetos e issues pré-selecionados
* Será feita em duplas/trios duas vezes
	* cada vez um será o responsável
	* ajudar a desempacar
* Teremos 2,5 aulas dedicadas para esta primeira contribuição

---

# Minha primeira contribuição de código

![](meu-pr.png)

-----

# Dicas para debugar (qualquer coisa)

![](livro.jpg)

---

# 9 regras de debug

1. UNDERSTAND THE SYSTEM
1. MAKE IT FAIL
1. QUIT THINKING AND LOOK
1. DIVIDE AND CONQUER
1. CHANGE ONE THING AT A TIME
1. KEEP AN AUDIT TRAIL
1. CHECK THE PLUG
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

# 1. Understand the system

## Conheça suas ferramentas

* Debugging visual linha a linha
* Stacktrace
* Busca em projeto inteiro
* Ir para definição de função

### Debugar usando `print` é perda de tempo

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

Comando `grep` ([man page](https://linux.die.net/man/1/egrep))

> `$ grep [OPTIONS] PATTERN FILES`

* `PATTERN`: expressão regular
* `FILES`: lista de diretórios ou arquivos

---

# 3. Quit thinking and look - grep

**Exemplo 1**: buscar todos arquivos nas pasta atual (.) e subpastas com o texto "dialog" ignorando maiúsculas/minúsculas.

> `$ grep -r -i dialog .`

#

**Exemplo 2**: Listas todos os arquivos *.cpp* que fazem algum include

> `$ grep -r --include "*cpp" "#include" .`

### Sua IDE/editor devem ter algo parecido. Procure e use.

----

# 4. Divide and Conquer

## Crie um plano de ação

1. Por que o bug ocorre? 
	- Está relacionado a qual função? 
	- Qual variável tem o valor errado?
2. O que deve ser mudado para que pare de ocorrer?


**Pré-requisito**: debugar visualmente usando alguma IDE / editor

----

# 5. Change one thing at a time

## Um bom PR muda o mínimo possível

* use várias branches se quiser testar ideias diferentes
* `git commit` é grátis. Quando chegar na versão final é só juntar tudo e mandar. 
* `git rebase` para atualizar seu branch com o `master upstream` caso necessário.


----

# 6. KEEP AN AUDIT TRAIL

## Registre suas descobertas

- Log de como você encontrou onde mexer
- Log de todos arquivos de interesse e seus usos
- Log de todas as pesquisas feitas
- Log de todas as modificações feitas
- `git commit` é útil para registrar testes também

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

### Tentem aplicar estas ideias aos seus problemas


----

Desenvolvimento Aberto
===

# ![width:300px](capa.svg)

##### Explorando seu projeto 


###### Igor dos Santos Montagner ( [igorsm1@insper.edu.br](mailto:igorsm1@insper.edu.br) )
