from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Use SQLite on the development box as a default. Using DATABASE_URL variable
# will override this setting.
try:
    DATABASES
except NameError:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

try:
    from .local import *
except ImportError:
    pass
