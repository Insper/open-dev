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
        'package1>=1.0',
        'package2'
    ],
    ...
~~~


!!! exercise
    Check the code dependencies and add them to `setup.py`...

### requirements.txt
 
Many software also use a *requirements.txt* file to list **all** software dependencies in order to obtain a installation identical to that of developer. This is important to standardize development environments. This file will never be used by end users.

!!! exercise
    Create a *requirements.txt* file for your project with the same dependencies listed on your *setup.py*. 

### Runnable Scripts

In addition to install our module for using `import`, we also want to make *hello.py* file available as an executable file for entire system. This can be done by adding the following line to our *setup.py* indicating that *scripts/hello.py* should be installed as an executable.

~~~
    ...
    scripts=['scripts/hello.py'],
    ...
~~~
            
Don't forget to add the following line to the top of your file so it can be run directly from shell:

~~~
#!/usr/bin/env python3
~~~

On Windows, an executable is created that runs our script, so that executable calls will work normally. Note that this does not create any type of graphical interface.

### Creating distribution files

Two types of distribution files can be used:

- **sdist**: This file  contains project's source code, including additional files specified by using `data_files` argument. This is used if your project is pure Python (only written in Python).
- **wheel**: This is a precompiled, platform-specific format. Most commonly used when the project contains *C language* extensions.

Creating a source code distribution file is quite simple:

<ah-terminal>
$ python setup.py sdist
</ah-terminal>

This package can be installed by `pip`.

### Uploading to PyPI

Now let's upload our package to *Python Package Index*; so it can be installed directly by `pip`. To avoid cluttering the repository with temporary and test packages, we can use *TestPyPI*. Its entire infrastructure is the same as the official one, but it is cleaned regularly.

Visit [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/) and register yourself on *TestPyPI*.

After registration, we'll use the *twine* package (installable by *pip*) to upload:

<ah-terminal>
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
</ah-terminal>

You can then install your package from *TestPyPI* using the following command:

<ah-terminal>
$ pip install --index-url https://test.pypi.org/simple/ my_hello_pack
</ah-terminal>

### Submit your assignment

Submit your assignment by adding *Python Package* skill and including URL of your GitHub repository.

![Python Package Skill](skill-python.svg){ style="height:150px" }

**Objective**: First experience distributing Python software.

> "skill_id": 6, "metadata": {"url": "repo-your-package"}

## Distributing Software to End Users

Now we'll work (in pairs) on the *Challenge Server* again. Your job will be to create a Dockerfile that runs this software *completely*. In other words, container creation script must:

- [ ] install all system dependencies
- [ ] create database, if it is necessary
- [ ] add all users present in `users.csv` file, if it is necessary
- [ ] run server on host port `8080` 
- [ ] retain added data when restarting the container

### Deliver this assignment

Deliver your activity by adding skill *Dockerfile* according to template below:

![Skill Dockerfile](skill-docker.svg){ style="height:150px" }

**Objective**: Create an automated deployment for a Python web system

> "skill_id": 7, "metadata": {"url": "challenge-server-repo", "group": ["login1", "login2"]}

### References

Some references that may be useful:

* [https://docker-curriculum.com/](https://docker-curriculum.com/)
* [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)
