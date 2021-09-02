# 05 - Projeto Profissional

Existe um momento em que ele já soluciona um problema para o autor e começa a ficar claro que ele é de interesse de outras pessoas. Vamos considerar que o Servidor de Desafios chegou neste momento e transformá-lo em um projeto "profissional".

Seu trabalho neste roteiro será preparar o projeto para ser apresentado "oficialmente" a outros usuários. Ou seja, fará mudanças para melhorar a qualidade do código e criará uma página para o projeto apresentando-o e provendo instruções de instalação e uso. 

Para entregar esta tarefa você deverá criar um repositório softdes-desafios em seu usuário, colocar o servidor de desafios lá e hospedar sua documentação usando [Github Pages](https://pages.github.com/). Com isto pronto envie o trabalho de vocês via PR para o repositório da disciplina. 

Os itens obrigatórios são descritos nos itens abaixo. 


# Itens básicos de qualidade

- [ ] Adicionar um README ao projeto
    - [ ] Adicione uma descrição do projeto
    - [ ] Screenshot
    - [ ] Links para docs de Desenvolvimento e Usuário
- [ ] Organizar pastas seguindo uma estrutura em que o código está em `src` e a documentação oficial em `docs`
- [ ] Subir código no Github

# Qualidade de código

Nosso código está mal formatado e tem várias práticas ruins de programação. O [pylint](https://www.pylint.org/) detecta estes problemas e dá uma nota para seu código. Melhore a nota do Servidor de Desafios eliminando estes problemas do código. Alguns dos problemas são de resolução simples e podem ser feitos por ferramentas, mas outros requerem uma atenção "humana"

Ele não precisa estar 100%, mas você precisa eliminar grande parte dos erros mais bizarros. Após fazer as correções crie um novo commit e prossiga.

!!! danger
    Certifique-se que o projeto continua funcionando! Alguns erros, como usar `exec` ou `eval` são inerentes ao projeto e não podem ser "consertados".

# Documentação

O [mkdocs](https://www.mkdocs.org/) é uma ferramenta de documentação de software para gerar uma página web de documentação para o projeto. Vamos usá-lo para documentação de desenvolvimento e de usuário do nosso projeto.

!!! tip
    O mkdocs possui vários temas. Escolha um que você goste.


## Documentação de usuário

Os seguintes itens devem estar presentes:

- [ ] Uma página inicial descrevendo o projeto e explicando seu uso esperado. Inclua links e screenshots do software rodando.
- [ ] Uma página de guia de usuário para alunos. Este guia deverá mostrar passo a passo as seguintes tarefa
    - [ ] entrar no servidor de desafios
    - [ ] enviar solução correta para desafio
    - [ ] enviar solução errada
- [ ] Uma página de guia de usuário para professores. Ela deverá descrever:
    - [ ] como adicionar usuários (usando os arquivos *users.csv* e *add_user.py*)
    - [ ] como adicionar novos desafios (linha de comando mesmo)

## Documentação de desenvolvimento

As seguintes informações devem estar presentes:

- [ ] como configurar ambiente de desenvolvimento
- [ ] instalação do software
- [ ] estrutura do código em alto nível
