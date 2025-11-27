#!/usr/bin/env python3
import os
import gettext
gettext.bindtextdomain('hello', 'locale')
gettext.textdomain('hello')
_ = gettext.gettext
from datetime import date, datetime
from dev_aberto import hello as get_commit_info

# Install gettext translations
localedir = os.path.join(os.path.dirname(__file__), 'locale')
gettext.bindtextdomain('hello', localedir)
gettext.textdomain('hello')
_ = gettext.gettext

# Helpers to get locale short code from environment variables like "pt_BR.utf8"
def _env_locale(varname, default='en_US'):
    val = os.environ.get(varname)
    if not val:
        return default
    # common formats: pt_BR.utf8 or en_US.UTF-8 or en_US
    for part in (val.split('.')[0], val.split('@')[0]):
        if part:
            return part
    return default

# Try to use Babel for nicer localized dates/numbers, but fall back if not installed.
try:
    from babel.dates import format_date
    from babel.numbers import format_decimal
    BABEL_AVAILABLE = True
except Exception:
    BABEL_AVAILABLE = False

def format_local_date(dt):
    # Determine locale from LC_TIME or LANG
    loc = _env_locale('LC_TIME', os.environ.get('LANG', 'en_US'))
    if BABEL_AVAILABLE:
        try:
            return format_date(dt, format='full', locale=loc)
        except Exception:
            return dt.isoformat()
    else:
        # fallback: use isoformat or simple strftime depending on locale
        try:
            # naive mapping for pt_BR
            if loc.startswith('pt'):
                return dt.strftime('%d de %B de %Y')
            else:
                return dt.strftime('%B %d, %Y')
        except Exception:
            return dt.isoformat()

def format_local_number(num):
    loc = _env_locale('LC_NUMERIC', os.environ.get('LANG', 'en_US'))
    if BABEL_AVAILABLE:
        try:
            return format_decimal(num, locale=loc)
        except Exception:
            return str(num)
    else:
        # fallback: pt uses comma as decimal separator and dot as thousand
        if loc.startswith('pt'):
            s = f"{num:,.4f}"
            return s.replace(',', 'X').replace('.', ',').replace('X', '.')
        else:
            return f"{num:,.4f}"

def parse_commit_date(commit_date_str):
    # GitHub returns strings like "2025-09-15T12:34:56Z"
    if not commit_date_str:
        return None
    s = commit_date_str
    if s.endswith('Z'):
        s = s[:-1] + '+00:00'
    try:
        dt = datetime.fromisoformat(s)
        return dt.date()
    except Exception:
        try:
            # try date portion only
            return date.fromisoformat(s.split('T')[0])
        except Exception:
            return None

def main():
    # Print today's date localized
    today = date.today()
    localized_today = format_local_date(today)
    print(_("Today's date: {date}").format(date=localized_today))

    # Print large fractional number localized
    number = 240000000000.32212
    localized_number = format_local_number(number)
    print(_("Number example: {number}").format(number=localized_number))

    # Ask user for name (translatable prompt)
    try:
        name = input(_("Input your name: "))
    except KeyboardInterrupt:
        print()  # newline
        return
    print(_("Hello {name}").format(name=name))

    # Attempt to fetch last commit info from GitHub (non-fatal if offline)
    try:
        commit_date_str, author_name = get_commit_info()
        commit_date = parse_commit_date(commit_date_str)
        if commit_date:
            commit_date_local = format_local_date(commit_date)
        else:
            commit_date_local = commit_date_str or _('unknown')
        print(_("Last commit made on: {date} by {name}").format(date=commit_date_local, name=author_name))
    except Exception as e:
        # Don't crash if requests/internet is not available; show a translated message.
        print(_("Could not fetch last commit info. (offline or network error)"))

if __name__ == '__main__':
    main()
