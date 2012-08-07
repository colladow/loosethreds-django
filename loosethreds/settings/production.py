import os
import json

ROOT_PATH = os.path.dirname(os.path.realpath(os.path.join(__file__, '..', '..')))
SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))

DB_FILE = open(os.path.join(SETTINGS_DIR, 'production-db.json'))
DB_INFO = json.loads(DB_FILE.read())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DB_INFO['name'],                      # Or path to database file if using sqlite3.
        'USER': DB_INFO['user'],                      # Not used with sqlite3.
        'PASSWORD': DB_INFO['password'],                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/colladow/webapps/static/loosethreds/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://static.colladow.com/loosethreds/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/colladow/webapps/static/loosethreds/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://static.colladow.com/loosethreds/static/'
