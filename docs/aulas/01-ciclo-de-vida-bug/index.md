# 01 - Workflow de desenvolvimento distribuído


Neste roteiro trabalharemos no workflow padrão para contribuir com
projetos hospedados no Github (mas que também serve para projetos git em
geral). Antes de começar cada aluno deverá localizar no github da
disciplina a issue correspondente a criação de seu usuário.

Nosso fluxo de trabalho será baseado em três grandes partes. Na primeira
será criada uma cópia do repositório insper/dev-aberto onde faremos
todas as mudanças necessárias. Na segunda enviaremos nossas modificações
para o repositório original usando um *Pull Request*, que é um pedido de
aceite das mudançás de um *fork* no repositório original. Por último,
atualizaremos nosso *fork* com modificações enviadas pelos colegas.

Alguns pontos a serem destacados no fluxo de trabalho acima:

1.  Mesmo que um usuário não tenha acesso ao repositório original ele
    pode trabalhar em sua cópia e somente quando tudo estiver pronto
    enviar suas modificações ao repositório original.
2.  É necessário que um desenvolvedor do projeto original "se
    responsabilize" pelas modificações externas aceitas.
3.  A aba *Pull requests* permite que os desenvolvedores discutam as
    propostas de modificações e as melhorem. Todo commit feito após a
    criação do PR é incluido e pode ser testado por qualquer um.

## Criando uma cópia própria

Iremos começar nosso fluxo de trabalho criando um *fork* do repositório
insper/dev-aberto. Todas nossas modificações serão feitas no nosso
*fork* em um branch separado (o correto é sempre usar um branch
diferente para cada issue). Desta maneira nossas modificações ficam
completamente isoladas do código original e podemos testá-las lado a
lado com o código original.

Primeiro, crie o *fork* via interface do Github. Depois, clone seu fork
e crie um novo branch chamado *issue-X*, onde *X* é o número da sua
issue no projeto original.

    $ git checkout -b issue-X

Para garantir que você está no diretório do seu fork, execute o comando:

    $ git remote -vv

Os endereços mostrados devem ser os do seu *fork*, não os do projeto
original.

Com o *fork* criado e estando no branch *issue-X* (você pode checar
usando git branch e mudar usando git checkout issue-X), vamos começar a
realizar modificações.

### Interagindo com o repositório da disciplina

A criação de usuários e adição de skills é feita usando o comando
`dev-aberto.py`. 

!!! tip
    Para utilizá-lo é necessário instalar os pacotes listados
no arquivo requirements.txt. 

Sua execução no terminal deverá listar os
comandos disponíveis.

    $ python3 dev-aberto.py

Para checar se tudo está funcionando direito, liste todos os usuários
cadastrados. Só deverá ter um usuário cadastrado (`fabriciojb`).

### Criando um usuário

A criação de usuários é feita com o comando:

    $ python3 dev-aberto.py new-user

Isto criará 3 arquivos na pasta \`students\`:

-   `seu-login`: informações básicas do usuário em formato JSON.
-   `seu-login-achievements`: arquivo criptografado contendo as entregas de
    cada aluno em formato JSON.
-   `seu-login.key`: chave criptográfica do arquivo acima.

Verifique que seu usuário foi criado corretamente listando novamente os
usuários existentes. Seu usuário deverá apresentar um \* ao lado do
nome, o que significa que o arquivo login.key está presente no sistema.

!!! danger
    Você não deverá incluir em seu PR o arquivo `*.key`. Ele deverá ser
    enviado por email para o professor. Faça isto agora antes que esqueça!

Verifique também que você consegue usar o comando `dev-aberto.py compute-grade seu-login`. Se
estiver tudo ok, passe para o próximo item.

### Adicionando uma skill

Com o usuário criado podemos adicionar a skill *Primeiros passos*. Você
já deve ter notado que a chave do professor está disponível (arquivo
`students/fabriciojb.key`). Isto foi feito para que vocês possam ter ao
menos um exemplo de como cada skill deverá ser adicionada. Veja abaixo
um exemplo de como a skill deverá ser incluida:

    $ python3 dev-aberto.py edit-achievements fabriciojb

Isto abrirá um arquivo para edição no *Vi*. Veja o formato usado para
incluir a skill e faça o mesmo para o seu usuário.

!!! tip
    Se você quiser usar outro editor de texto pode setar a variável de
    ambiente `EDITOR` logo antes de chamar o `dev-aberto.py`.


Agora adicione a skill no seu usuário seguindo o mesmo padrão visto acima. Confira que sua skill foi corretamente adicionada usando o comando
compute-grade.

!!! tip
    Se seu repositório estiver *OK* ajude seus colegas

## Enviando as modificações para o projeto original

Vamos agora criar um commit e enviá-lo como *Pull Request* para o
repositório da disciplina. Adicione os arquivos criados (menor o arquivo
`*.key`!) e faça um commit com a seguinte mensagem (substituindo o *X*
pelo número da sua issue no repositório):

    Adiciona usuário seu-login.

Execute um `git push` e continue.

Com as suas modificações já presentes no seu *fork* é hora de enviá-las
para o repositório original. Isto é feito na interface do Github.
Primeiro, acesse seu *fork* no navegador, localize seu branch *issue-X*
e clique no botão "Pull request".

![Esta mensagem aparece quando seu *fork* tem commits que não estão
presentes no repositório original.](PR-github.png){width="90%"}

O título de seu Pull Request deverá ser *Cria usuário login*. Seu PR
deverá conter somente um commit e deverá ter como origem o branch
`issue-X` criado acima. Na descrição do seu PR, adicione o texto

    Closes #X

onde `X` é o número da issue de seu usuário. Isto faz com que a issue seja automaticamente fechada quando (e se) este PR for aceito. 


!!! warning
    Não serão aceitos PRs feitos a partir do `main` nem que tenham mais de um commit.

Use o checklist abaixo para ajudar a verificar se o seu trabalho está correto:

 - [ ] criou usuário novo com `new-user`
 - [ ] adicionou a skill "Primeiros passos"
 - [ ] checou se o usuário novo está com a nova skill usando `compute-grade`
 - [ ] criou PR contendo somente um commit e com os arquivos corretos
 - [ ] enviou arquivo `.key` por email para o professor
 - [ ] não adicionou arquivo `.key` no PR

Assim que seu PR for aceito você pode remover o branch issue-X.

## Atualizando seu *fork*

Ao ter seu PR aceito você deve ter notado que seu commit aparece no
`main` do projeto original mas não aparece no seu fork. Isto ocorre
pois um fork não é automaticamente atualizado quando seu repositório
original correspondente receber novos commits. 

Para que isto ocorra é necessário realizar a sincronização *manualmente*. Por enquanto vamos nos contentar em usar a interface do Github para fazer isto. 

Visite novamente seu *fork*. Agora deverá aparecer uma opção para sincronizar seu *fork* com o repositório original. Use-a para fazer com o que o seu `main` receba os novo commits. 

!!! warning
    Sincronize seu repositório sempre que for trabalhar em um novo PR. Isso evitará muitos conflitos na hora de juntar suas modificações ao repositório original.
