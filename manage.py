#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Role_based_login_system.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


def set_strict_sql_mode(sender, **kwargs):
    from django.conf import settings
    if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.mysql':
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute('SET session sql_mode=traditional')


from django.core.signals import request_started

request_started.connect(set_strict_sql_mode)
