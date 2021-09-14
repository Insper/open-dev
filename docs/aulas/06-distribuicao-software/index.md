# 06 - Distribuição de Software

Nesta aula complementaremos as últimas discussões criando um pequeno pacote Python instalável via `pip`. Com isto chegamos mais perto de um projeto que esteja preparado para que outras pessoas o utilizem e colaborem em seu desenvolvimento. 

## Distribuindo software para desenvolvedores: pacote Python básico

Nosso módulo se chamará `dev_aberto` e disponibilizará um programa executável `hello.py`. Crie a seguinte estrutura de pastas para nosso pacote. 

!!! important
    Baixe os arquivos que usaremos [neste link](https://github.com/Insper/dev-aberto/tree/master/docs/aulas/06-distribuicao-software)

~~~
pacote_exemplo/
    dev_aberto/
        __init__.py
        dev_aberto.py
    scripts/
        hello.py
    README.md
    LICENSE
~~~

!!! exercise
    com a estrutura acima, qual seria o `import` a ser feito para usar a função `hello` do arquivo *dev_aberto.py*?

!!! exercise
    Pesquise para que serve o arquivo **`__init__.py`** e use-o para permitir importar `hello` usando somente `import dev_aberto`.

!!! exercise
    Crie um projeto no github para esta atividade. Faça um primeiro commit nele com o conteúdo "zerado" do projeto.

    - Um arquivo *README* contendo uma frase de descrição do pacote e um link para o repositório da disciplina. 
    - Um arquivo *LICENSE* com a licença MIT. 


### O arquivo `setup.py`

A descrição de um pacote Python é feita usando um arquivo setup.py  Veja abaixo uma versão inicial deste arquivo:

~~~{.py}
from setuptools import setup

setup(name='dev_aberto_seunome',
      version='0.1',
      packages=['dev_aberto']
      )
~~~

!!! exercise
    Crie o arquivo acima no seu projeto, substituindo *seunome* por .... seu nome. Instale o seu próprio pacote usando 

    > pip install .
    
!!! exercise
    Em outra pasta, abra um console Python e tente importar seu módulo. 

!!! exercise
    Pesquise quais argumentos são usados para especificar o autor do pacote, as versões de Python e sistemas operacionais suportados. Preencha estes valores com suas informações. Note que o `pip` leva estas informações em conta e só instalará um pacote se ele estiver em um ambiente suportado. 

### Dependências

Para adicionar pacotes que são automaticamente instalados quando instalamos nosso pacote precisamos identificá-los no nosso arquivo *setup.py*. Para adicionar uma dependência de instalação basta adicionar o seguinte argumento:

~~~
    ...
    install_requires=[
        'pacote>=1.0',
        'pacote2'
    ],
    ...
~~~


!!! exercise
    Verifique as dependências do código e adicione-as no `setup.py`. 

### requirements.txt

Muitos softwares usam também um arquivo *requirements.txt* para listar **todas** as dependências do software de modo a obter uma instalação idêntica à do desenvolvedor. Isto é importante para uniformizar os ambientes de desenvolvimento. Ou seja, este arquivo nunca será usado por usuários finais. 

!!! exercise
    Crie um *requirements.txt* para seu projeto com as mesmas dependências listadas no seu *setup.py*. 

### Scripts executáveis

Além de instalar o nosso módulo para uso via `import` desejamos também disponibilizar o arquivo *hello.py* como um executável para todo o sistema. Isto pode ser feito adicionando a seguinte linha no nosso *setup.py* indicando que *scripts/hello.py* deverá ser instalado como um executável. 

~~~
    ...
    scripts=['scripts/hello.py'],
    ...
~~~

Não se esqueça de adicionar a seguinte linha no topo de seu arquivo para que ele possa ser executado diretamente do shell:

~~~
#!/usr/bin/env python3
~~~

No Windows é criado um executável que chama nosso script, de modo que as chamdas do executável continuarão funcionando normalmente. Note que isto não cria menus em nenhum tipo de interface gráfica. 

### Criando arquivos de distribuição

Dois tipos de arquivos de distribuição podem ser usados:

- sdist: é um arquivo contendo os fontes do projeto, incluindo arquivos adicionais especificados usando o argumento `data_files`. Usado se seu projeto for Python-puro.
- wheel: é um formato pré-compilado e específico para cada plataforma. Mais usado quando o projeto contém extensões em *C*.

A criação de um arquivo de distribuição de fontes é bem simples:

    > python setup.py sdist
    
A instalação deste pacote pode ser feita via `pip`.

### Envio para o PyPI

Vamos agora enviar nosso pacote para o *Python Package Index* para que ele possa ser instalado diretamente via `pip`. Para não poluir o repositório com pacotes temporários e de teste, podemos usar o *TestPyPI*. Toda sua infraestrutura é igual ao oficial, mas ele é limpo de maneira regular. 

Visite [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/) e registre-se no *TestPyPI*.

Após o registro, usaremos o pacote *twine* (instalável via *pip*) para fazer o upload:

    > twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Você poderá, então, instalar seu pacote a partir do test PyPI usando o seguinte comando:

    > pip install --index-url https://test.pypi.org/simple/ my_hello_nome

### Entrega

Faça a entrega de sua atividade adicionando a skill *Pacote Python* e inclua nela a url do seu repositório no github.

![Skill Pacote Python](skill-python.svg){ style="height:150px" }

**Objetivo**: Primeira experiência distribuindo software Python.

> "metadata": {"url": "repo-seu-pacote"}

## Distribuindo software para usuários finais

Vamos agora trabalhar (em grupo) no Servidor de Desafios novamente. Seu trabalho será criar um `Dockerfile` que roda o software de maneira "completa". Ou seja, o script de criação do container deverá

- [ ] instalar todas as dependências do sistema
- [ ] criar a base de dados, se necessário
- [ ] adicionar os usuários presentes no arquivo `users.csv`, se necessário
- [ ] executar o servidor e serví-lo na porta `8080` do `host`
- [ ] manter os dados adicionados ao reiniciar o container

### Entrega

Faça a entrega de sua atividade adicionando a skill *Dockerfile* segundo o modelo abaixo.

![Skill Dockerfile](skill-docker.svg){ style="height:150px" }

**Objetivo**: Criou deploy automatizado para sistema web Python

> "metadata": {"url": "repo-servidor-de-desafios", "group": ["login1", "login2"]}