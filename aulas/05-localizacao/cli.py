from babel import dates
from babel import numbers
from datetime import date
from datetime import date, datetime, time
import gettext

gettext.install('cli', localedir='locale')

if __name__ == '__main__':
    today = date.today()
    data = dates.format_datetime(today)
    print(data)

    number = 240000000000.32212
    number = numbers.format_number(number)
    print(number)
    
    name = input(_('Input your name: '))
    print(_('Hello {}').format(name))

