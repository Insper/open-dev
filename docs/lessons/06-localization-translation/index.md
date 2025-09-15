# 06 - Localization and Translation

<ah-external-content src="slides.html" />

In lecture section, we introduced issues of Internationalization (I18N) and Localization (L10N). In this tutorial, we will practice using these techniques in a simple command-line application.

In both examples, we will work with *Babel* module, which is designed to facilitate translation and localization of Python applications. Other programming languages ​​have similar libraries that follow the same command sequence and use the same file types.

<ah-terminal>
$ pip install Babel
</ah-terminal>

POSIX systems support determining *locale* through environment variable *LANGUAGE*, which can be modified for each running program. Default format is `<language>_<country>.<encoding>`. For Brazilian Portuguese using UTF8 encoding, we use the `pt_BR.utf8` locale. Running the following command, help messages for `ls` command should appear in English.

<ah-terminal>
$ LANGUAGE=en_US.utf8 ls --help
</ah-terminal>

Running command below, messages should appear in Portuguese.

<ah-terminal>
$ LANGUAGE=pt_BR.utf8 ls --help
</ah-terminal>

More generally, there are many *LC_\** variables that control which locale is used for a given data type. We'll see below how to use `LC_TIME` and `LC_NUMERIC` to control how dates and numbers are displayed, and `LANGUAGE` to set a program's display language.

## Localizing a Python Program
 
We'll work with a command-line application that does nothing more than print some simple data, such as a date in full, a large fractional number, and a predefined message. The complete code (*cli.py* file) is below.

```python
from datetime import date

if __name__ == '__main__':
    today = date.today()
    print(today)

    number = 240000000000.32212
    print(number)

    name = input('Input your name: ')
    print('Hello {}'.format(name))
    
```

A possible output would be

```
2025-09-15
240000000000.3221
Input your name: Carlos
Hello Carlos
```

As already seen in class, this program combines three of the main outputs that need to be formatted: dates, fractional numbers, and messages to user.

## Formatting Dates

Date formatting is ruled by `LC_TIME` variable. `babel.dates` module already has several functions that automatically use `LC_TIME` to locate variables of the `Date` type (using the `format_date` function) or `DateTime` (using `format_datetime`).

!!! exercise
    Research about how to use these functions and use them in your program to locate date in full (i.e., August 31, 2021).

!!! exercise
    What happens when we set environment variable `LC_TIME=en_US.utf8` and run the program? What if we use `LC_TIME=pt_BR.utf8`?

## Formatting Numbers

Date formatting is ruled by `LC_NUMERIC` variable. `babel.numbers` module has the `format_number` function that formats a number according to this setting.

!!! exercise
    Research how to use these functions and use them in your program to locate that fractional number.

!!! Exercise
    Test your program with `LC_NUMERIC=en_US.utf8` and `LC_NUMERIC=pt_BR.utf8`. Are the results as expected?

## Translating Messages

The final step consists of creating translations of those two strings. Language used is defined by `LANGUAGE` variable, which can be defined separately for each process. One of the most important points is to mark which strings should be translated, so translators don't need to change the code. Python `gettext` module already supports this functionality; *Babel* simply provides a set of tools that facilitate its use.

Implementing the translation framework is done in four steps:

1. Marking the strings to be translated
1. Extracting these strings from code to a `.pot` template file
1. Creating `.po` translations from the template created in the previous step
1. Compiling translated strings to a `.mo` binary file

In main file of our application we can "install" translation framework and mark all strings will be translated with the `_()` function. Installation is done with the following code snippet.

```python
import gettext
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

# cli: name of the file where we save our translations
# localedir: path where the translations are stored. It can be a relative path.
```

Then we must mark all strings to be translated with `_()`. We can use `_()` in any project file, even if the installation was only done in the main file.

```python
print(_("Hello!"))
```

The following steps are done with *Babel*'s help, which effectively analyzes our Python code and extracts all strings for translation. The following command is used to create translation model file from files in current directory:

<ah-terminal>
$ pybabel extract . -o cli-model.pot
</ah-terminal>

So we create a new translation using the command bellow. `-D` option indicates the name of file where the translations will be saved (used in `gettext.install`). `-l` option indicates translation locale. `-d` option indicates `localedir` used in `gettext.install`.

<ah-terminal>
$ pybabel init -i cli-model.pot -D cli -l pt_BR -d locale
</ah-terminal>

We must then edit created file in *locale/pt_BR/LC_MESSAGES/cli.po*. Pairs of lines like the following will be displayed (after a few lines of comments). First value (`msgid`) is the string to be translated and the second (`msgstr`) is the translation in the *pt_BR* locale (since file is in the pt_BR folder of localedir).

```
msgid "Input your name: "
msgstr ""
```

Although it's possible to do everything by directly editing text file, it's more convenient to use a software like [poedit](https://poedit.net/) or this [online editor](https://localise.biz/free/poeditor)(https://localise.biz/free/poeditor).

We'll finally compile our results after translate strings. This compile process is done so that it won't be possible to tamper with translation files in a *Release* version of the program.

<ah-terminal>
$ pybabel compile -D cli -l pt_BR -d locale
</ah-terminal>

This will generate `.mo` files corresponding to `pt_BR` locale. These files are loaded during program execution.

## Final Test

We can set `LANGUAGE` variable to change program's language (as seen previously with `ls`). Run your program directly and then run it setting `LANGUAGE=pt_BR.utf8`. Were the results as expected?

## Submission

Modify the previous class exercise (python package) to support dates and messages in English and Portuguese. Submit your assignment by adding the *Basic Translation* skill according to template below.

![Skill Tradução básica](skill-traducao.svg){ style="height:150px" }

**Objective**: To test localization tools to translate a simple command-line program.

> "skill_id": 8, "metadata": {"url": "repo-pacote-python"}
