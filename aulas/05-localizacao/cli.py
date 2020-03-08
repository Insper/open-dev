import babel
from datetime import date
from datetime import date, datetime, time

if __name__ == '__main__':
    today = date.today()
    print(today)

    number = 240000000000.32212
    print(number)
    
    name = input('Input your name: ')
    print('Hello {}'.format(name))