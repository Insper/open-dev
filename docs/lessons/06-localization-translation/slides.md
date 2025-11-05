---
marp: true
title: Software Translation and Localization
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

Open Development
===

![width:300px](capa.svg)

##### Software Localization and Internationalization


###### Version 2023/2: Igor Montagner (igorsm1@insper.edu.br)


---
# Software Translation

## What is the difference between internationalization and localization?

---
# Internationalization (I18N)

- This involves translating a software's user interface into other languages.

- Operating system saves language settings and makes them available to applications.

- "Invisible" typically.


---
# Localization (L10N)

This involves adapting the way it displays:

- fractional numbers
	- decimal placeholders
	- thousands placeholders
- dates
	- month names
	- display order
- country names, time zones, etc.

according to a user's preferences and cultural preferences.

--- 
# I18N and L10N

They must be

- independent:
	- English language and dates in Brazilian format
- configurable:
	- I may need to switch between languages ​​and formats

### Support for L10N and I18N involves modifying source code.

---
# Locales

A *locale* is a triple

#

	<language>_<country>.<encoding>

#

that represents I18N and/or L10N settings for a given culture.

---
# Locales

Examples:

- Translation of *File* word:
	- `pt` = Ficheiro
	- `pt_BR` = Arquivo
- Date format:
	- `en_US`: *MM/DD/YY*
	- `en_GB`: *DD/MM/YY*

### I can use different *locales* for the user interface language and for displaying dates.

---

# Possible configurations (Linux)

```
# output of locale command
LANG=en_US.UTF-8
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC=pt_BR.UTF-8
LC_TIME=pt_BR.UTF-8
LC_COLLATE=pt_BR.UTF-8
LC_MONETARY=pt_BR.UTF-8
LC_MESSAGES="en_US.UTF-8"
LC_PAPER=pt_BR.UTF-8
LC_NAME=pt_BR.UTF-8
LC_ADDRESS=pt_BR.UTF-8
LC_TELEPHONE=pt_BR.UTF-8
LC_MEASUREMENT=pt_BR.UTF-8
LC_IDENTIFICATION=pt_BR.UTF-8
```

---
# Implementing L10N support

1. Download a localization library
2. Find all numbers, dates, etc ... displays
3. Preprocess them using library functions

#
```python
# Before
print('Number:', 10.5)
# After
print('Number', format_number(10.5))
```
#

It's not complicated, but it is **laborious**

---
# I18N Support

Involves 4 steps:

1. Mark all strings that should be translated
2. Extract them from the source code
3. Create a translation file for each supported locale
4. Package translations with program

#

It's a bit more complicated, but it can be integrated into a program's compilation process.

---
# I18N Support (POSIX)

POSIX systems support determining language and locale by using environment variables.

- `LANG` for language
- `LC_TIME` for date
- `LC_NUMERIC` for numbers



A locale is always expressed in the format

<language>_<country>.<encoding>

---
# I18N support (POSIX)

`locale` command displays all available options:

```
# locale command output
LANG=en_US.UTF-8
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC=pt_BR.UTF-8
LC_TIME=pt_BR.UTF-8
LC_COLLATE=pt_BR.UTF-8
LC_MONETARY=pt_BR.UTF-8
LC_MESSAGES="en_US.UTF-8"
LC_PAPER=pt_BR.UTF-8
LC_NAME=pt_BR.UTF-8
LC_ADDRESS=pt_BR.UTF-8
LC_TELEPHONE=pt_BR.UTF-8
LC_MEASUREMENT=pt_BR.UTF-8
LC_IDENTIFICATION=pt_BR.UTF-8
```
---
# I18N support (Web)

There are several ways to determine a good locale on Web systems:

- HTTP header `Accept-Language` includes ​​supported display languages by visitor's browser.
- Geolocation *via* IP
- Preference stored in a database

#

#### Web and desktop use the same technologies (L10N and I18N)

---
# I18N support (in Python)

- `gettext` module from the standard library
- `datetime` module supports locales
- `babel` module supports I18N and L10N

----

# Practical activity: Basic translation

![width:256px](skill-traducao.svg)

**Objective**: Use *Babel* module to translate a terminal (console) application.

---
Open Development
===

![width:300px](capa.svg)

##### Software Localization and Internationalization

###### Version 2023/2: Igor Montagner (igorsm1@insper.edu.br)
