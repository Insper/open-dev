from babel.numbers import *
from babel.dates import *
from datetime import date
from datetime import date, datetime, time
import gettext

gettext.install('cli', localedir='locale')


if __name__ == '__main__':
    today = date.today()
    print(format_date(today))

    number = 240000000000.32212
    print(format_number(number))
    
    name = input(_('Input your name: '))
    print(_('Hello {}').format(name))
