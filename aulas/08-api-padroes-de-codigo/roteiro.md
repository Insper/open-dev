% 08 - Documentação de código e lintes
% Desenvolvimento Aberto - 2019/2
% Igor Montagner
 
Na parte expositiva da aula vimos mais um elemento que torna nosso código um projeto funcional e útil para outras pessoas: documentação de *API*. Até agora já trabalhamos:

1. traduções de interface de usuário e localização
1. documentação de usuário
2. documentação de desenvolvedor
    * referência de *API*

Claro que nem todo projeto precisa começar com tudo isso, mas existe um momento em que ele já soluciona um problema para o autor e começa a ficar claro que ele é de interesse de outras pessoas. Vamos considerar que o Servidor de Desafios chegou neste momento. 

Seu trabalho neste roteiro será preparar o projeto para ser apresentado "oficialmente" a outros usuários. Ou seja, fará mudanças para melhorar a qualidade do código e criará uma página para o projeto apresentando-o e provendo instruções de instalação e uso. 

# Parte 1 - qualidade de código

Nosso código está mal formatado e tem várias práticas ruins de programação. O [pylint](https://www.pylint.org/) detecta estes problemas e dá uma nota para seu código. Melhore a nota do Servidor de Desafios eliminando estes problemas do código. 

Ele não precisa estar 100%, mas você precisa eliminar grande parte dos erros mais significativos. 

# Parte 2 - trabalhando com Sphinx

Agora vamos trabalhar com [sphinx](https://www.sphinx-doc.org/en/master/) para gerar uma página web de documentação para o projeto. As seguintes páginas deverão ser criadas.

* Uma página inicial descrevendo o projeto
* Uma página de guia de usuário para alunos
* Uma página de guia de usuário para professores
* Uma página de guia de desenvolvimento listando bibliotecas, procedimentos para instalação e estrutura em alto nível do código
* Uma seção com a documentação de cada função do projeto usando [sphinx-apidoc](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html).

Siga o guia [Getting Started](https://www.sphinx-doc.org/en/master/usage/quickstart.html) para criar sua página de documentação. 

# Entrega

Ao terminar este trabalho você deverá criar um repositório softdes-desafios em seu usuário, colocar o servidor de desafios lá e hospedar sua documentação usando [Github Pages](https://pages.github.com/). Envie a skill *Projeto profissional*, colocando no campo *metada* um link para a sua página hospedada. 