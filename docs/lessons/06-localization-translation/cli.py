from datetime import date
from babel.dates import format_date, format_datetime, format_time
from babel.numbers import format_number, format_decimal
import gettext
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext
# cli é o nome do arquivo em que guardamos nossas traduções
# localedir é o caminho onde estão armazenadas as traduções. Pode ser um caminho relativo. 

if __name__ == '__main__':
    today = date.today()
    print(format_date(today, format='short'))

    number = 240000000000.32212
    print(format_decimal(number))
    
    name = input(_('Input your name: '))
    
    print(_('Hello {}').format(name))