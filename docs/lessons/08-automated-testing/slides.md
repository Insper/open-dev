---
marp: true
title: Automated Tests
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

![100%](capa.svg)

##### Automated Testing

###### Igor dos Santos Montagner ( [igorsm1@insper.edu.br](mailto:igorsm1@insper.edu.br) )

---

# Professional Project

- Code Quality
    - Linting - Formatting and Common Errors
- Documentation
    - User
    - Developer

---

# Professional Project

- Code Quality
    - Linting - Formatting and Common Errors
    - **Does the code work?**
- Documentation
    - User
    - Developer

----

# Does my program work?

- Under what conditions?
- On which platforms?
- Which operations are supported?
- Can I check the result of an execution? If so, is there a reference value?

---

# Automated Testing

**Idea**: Write a program that verifies whether another program responds as expected.

- Define situations to be tested...
- And the expected result in each situation.

---
# Automated Testing

**Doesn't help**

- Reveal new bugs
- Ensure software is bug-free

**Does help**

- Prevent discovered bugs from returning
- Prevent unintended changes from breaking previously working code.
- Document in which situations the software works.

---

# Automated Testing

1. Unit Testing
2. Integration Testing
3. User Interface Testing

---

# Unit Testing

**Idea**: Given a function, verify whether it returns the expected value for a given set of parameters.

- Test functions in **isolation**.
- **Coverage**: Percentage of lines of code executed during unit testing.
- Serves as function documentation


---
# Unit tests - pytest

![width:900px](pytest.png)

---

# Integration tests

**Idea**: Given a set of classes with interdependencies, verify that they work well **together**.

- Tests interaction between objects
- Possibility of creating *mocks*, which are fake objects designed to simulate the interaction between multiple objects.
----

# User interface tests

**Idea**: Simulates user actions (clicks, data entry, etc.) and checks if the expected output is displayed on the screen.

- Must be designed as minimally specific as possible
- Most faithful to a user's actual use

---

# User interface tests

## Selenium

Allows you to create scripts that interact with a web page, performing data entry, scrolling, and clicks. Each `assert` can be made with the content of a page object.

---

# What do I need to test?

## 

---


# What do I need to test?

## Nobody knows...

----

# Practical activity: Tested and approved


![width:256px](https://fonts.gstatic.com/s/i/materialicons/sentiment_very_satisfied/v4/24px.svg?download=true)

**Objective**: First experience with automated code testing.

> "metadata": {"url": "acceppted PR", "group": [ "the same of class 6" ]}
