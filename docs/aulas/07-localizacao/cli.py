# pylint: disable=missing-module-docstring
from datetime import date
from gettext import _

if __name__ == '__main__':
    today = date.today()
    print(today)

    number = 240000000000.32212
    print(number)
    
    name = input(_('Input your name: '))
    print('Hello {}'.format(name))