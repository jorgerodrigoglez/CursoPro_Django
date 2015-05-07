from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eventusdb',
        'USER': 'eventususer',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'

#para los archivos de imagenes con la libreria pillow
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media') #esta variable hay que modificarla en base.py, hay que instalar unipath pip install unipath
