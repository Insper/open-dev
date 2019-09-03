import babel
from datetime import date
from datetime import date, datetime, time
from babel.dates import format_date, format_datetime, format_time
from babel.numbers import format_number, format_decimal, format_percent

if __name__ == '__main__':
    today = date.today()
    print(today)
    newtoday = format_date(today, "long")
    print(newtoday)

    number = 240000000000.32212
    print(number)
    number = format_number(number)
    print(number)

    
    name = input('Input your name: ')
    print('Hello {}'.format(name))