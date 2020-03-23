% 08 - Documentação de código e linter
% Desenvolvimento Aberto - 2020/2
% Igor Montagner
 
Na parte expositiva da aula vimos mais um elemento que torna nosso código um projeto funcional e útil para outras pessoas: documentação de *API*. Até agora já trabalhamos:

1. traduções de interface de usuário e localização
1. documentação de usuário
2. documentação de desenvolvedor

Claro que nem todo projeto precisa começar com tudo isso, mas existe um momento em que ele já soluciona um problema para o autor e começa a ficar claro que ele é de interesse de outras pessoas. Vamos considerar que o Servidor de Desafios chegou neste momento. 

Seu trabalho neste roteiro será preparar o projeto para ser apresentado "oficialmente" a outros usuários. Ou seja, fará mudanças para melhorar a qualidade do código e criará uma página para o projeto apresentando-o e provendo instruções de instalação e uso. 

# Parte 1 - qualidade de código

Nosso código está mal formatado e tem várias práticas ruins de programação. O [pylint](https://www.pylint.org/) detecta estes problemas e dá uma nota para seu código. Melhore a nota do Servidor de Desafios eliminando estes problemas do código. 

Ele não precisa estar 100%, mas você precisa eliminar grande parte dos erros mais bizarros. 

# Parte 2 - trabalhando com Sphinx


Agora vamos trabalhar com [mkdocs](https://www.mkdocs.org/) para gerar uma página web de documentação para o projeto. As seguintes páginas deverão ser criadas.

* Uma página inicial descrevendo o projeto e explicando seu uso esperado. Inclua links e screenshots do software rodando.
* Uma página de guia de usuário para alunos. Este guia deverá mostrar passo a passo as seguintes tarefa
    * entrar no servidor de desafios
    * enviar solução correta para desafio
    * enviar solução errada
* Uma página de guia de usuário para professores. Ela deverá descrever:
    * como adicionar usuários (usando os arquivos *users.csv* e *add_user.py*)
    * como adicionar novos desafios
* Uma página de guia de desenvolvimento listando 
    * como configurar ambiente de desenvolvimento
    * instalação do software
    * estrutura do código em alto nível
* Uma documentação da *API* do software. Vocês podem usar o plugin [mkdocstrings](https://github.com/pawamoy/mkdocstrings) para converter as *docstrings* de cada *endpoint* do sistema em uma página de documentação bem formatada.    

# Entrega

Ao terminar este trabalho você deverá criar um repositório softdes-desafios em seu usuário, colocar o servidor de desafios lá e hospedar sua documentação usando [Github Pages](https://pages.github.com/). Com isto pronto envie o trabalho de vocês via PR para o repositório da disciplina. 