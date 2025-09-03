# 05 - Distribution of Software

In this lesson we will complement the latest discussions creating a small Python package installed via `pip`. With this we come closer to a project that is prepared for others to use and collaborate in its development.

## Distributing software to developers: basic Python package

Our module will be called `dev_aberto` and provide an executable program `hello.py`. Create the following folder structure for our package.

!!! important
    Download the files we will use at this [link](https://github.com/Insper/open-dev/tree/master/docs/lessons/05-python-packaging)

~~~
package_example/
    dev_aberto/
        __init__.py
        dev_aberto.py
    scripts/
        hello.py
    README.md
    LICENSE
~~~

!!! exercise
    Considering above structure, what would be the appropriate `import` command at a *Python* script to use `hello` function from *dev_aberto.py* file?

!!! exercise
    Search what **`__init__.py`** file is for and use it to allow import `hello` function using only `import dev_aberto`.


!!! exercise
    Create a project in github for this activity. Make a first commit to this project without programming content.

    - A *README* file containing a description phrase of the package and a link to discipline repository. 
    - A *LICENSE* file with MIT license. 

### File `setup.py`

Description of a Python package is made using a `setup.py` file. See below an initial version of this file:

~~~{.py}
from setuptools import setup

setup(name='dev_aberto_Your_Name',
      version='0.1',
      packages=['dev_aberto']
      )
~~~

!!! exercise
    Create the above file in your project by replacing *Your_name* by ... your name. Install your own package using

    > pip install .
    
!!! exercise
    In another folder, open a Python console and try to import your module. 

!!! exercise
    Find out what arguments are used to specify package author, Python versions, and supported operating systems. Fill these values with your information. Please note that `pip` take this information into account and will only install a package if it is in a supported environment.

### Dependencies

To add packages that are automatically installed when we install our package we need to identify them in our *setup.py* file. To add an installation dependency just add the following argument:

~~~
    ...
    install_requires=[
        'packaage1>=1.0',
        'package2'
    ],
    ...
~~~


!!! exercise
    Check the code dependencies and add them to `setup.py`...

### requirements.txt

Muitos softwares usam também um arquivo *requirements.txt* para listar **todas** as dependências do software de modo a obter uma instalação idêntica à do desenvolvedor. Isto é importante para uniformizar os ambientes de desenvolvimento. Ou seja, este arquivo nunca será usado por usuários finais. 
Many software also use a *requirements.txt* file to list **all** software dependencies in order to obtain a installation identical to that of developer. This is important to standardize development environments. This file will never be used by end users.

!!! exercise
    Create a *requirements.txt* file for your project with the same dependencies listed on your *setup.py*. 

### Runnable Scripts

Além de instalar o nosso módulo para uso via `import` desejamos também disponibilizar o arquivo *hello.py* como um executável para todo o sistema. Isto pode ser feito adicionando a seguinte linha no nosso *setup.py* indicando que *scripts/hello.py* deverá ser instalado como um executável. 

In addition to installing our module for use *via* `import`, we also want to make *hello.py* file available as an executable for entire system. This can be done by adding the following line to our *setup.py* indicating that *scripts/hello.py* should be installed as an executable.

~~~
    ...
    scripts=['scripts/hello.py'],
    ...
~~~
            
Não se esqueça de adicionar a seguinte linha no topo de seu arquivo para que ele possa ser executado diretamente do shell:

~~~
#!/usr/bin/env python3
~~~

No Windows é criado um executável que chama nosso script, de modo que as chamadas do executável continuarão funcionando normalmente. Note que isto não cria menus em nenhum tipo de interface gráfica. 

### Criando arquivos de distribuição

Dois tipos de arquivos de distribuição podem ser usados:

- sdist: é um arquivo contendo os fontes do projeto, incluindo arquivos adicionais especificados usando o argumento `data_files`. Usado se seu projeto for Python-puro.
- wheel: é um formato pré-compilado e específico para cada plataforma. Mais usado quando o projeto contém extensões em *C*.

A criação de um arquivo de distribuição de fontes é bem simples:

<ah-terminal>
$  python setup.py sdist
</ah-terminal>
    
A instalação deste pacote pode ser feita via `pip`.

### Envio para o PyPI

Vamos agora enviar nosso pacote para o *Python Package Index* para que ele possa ser instalado diretamente via `pip`. Para não poluir o repositório com pacotes temporários e de teste, podemos usar o *TestPyPI*. Toda sua infraestrutura é igual ao oficial, mas ele é limpo de maneira regular. 

Visite [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/) e registre-se no *TestPyPI*.

Após o registro, usaremos o pacote *twine* (instalável via *pip*) para fazer o upload:


<ah-terminal>
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
</ah-terminal>

Você poderá, então, instalar seu pacote a partir do test PyPI usando o seguinte comando:

<ah-terminal>
$ pip install --index-url https://test.pypi.org/simple/ my_hello_nome
</ah-terminal>

### Entrega

Faça a entrega de sua atividade adicionando a skill *Pacote Python* e inclua nela a url do seu repositório no github.

![Skill Pacote Python](skill-python.svg){ style="height:150px" }

**Objetivo**: Primeira experiência distribuindo software Python.

> "skill_id": 6, "metadata": {"url": "repo-seu-pacote"}

## Distribuindo software para usuários finais

Vamos agora trabalhar (em duplas) no Servidor de Desafios novamente. Seu trabalho será criar um `Dockerfile` que roda o software de maneira "completa". Ou seja, o script de criação do container deverá

- [ ] instalar todas as dependências do sistema
- [ ] criar a base de dados, se necessário
- [ ] adicionar os usuários presentes no arquivo `users.csv`, se necessário
- [ ] executar o servidor e serví-lo na porta `8080` do `host`
- [ ] manter os dados adicionados ao reiniciar o container

### Entrega

Faça a entrega de sua atividade adicionando a skill *Dockerfile* segundo o modelo abaixo.

![Skill Dockerfile](skill-docker.svg){ style="height:150px" }

**Objetivo**: Criou deploy automatizado para sistema web Python

> "skill_id": 7, "metadata": {"url": "repo-servidor-de-desafios", "group": ["login1", "login2"]}

### Referências

Algumas referências que podem ser úteis: 

* [https://docker-curriculum.com/](https://docker-curriculum.com/)
* [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)
