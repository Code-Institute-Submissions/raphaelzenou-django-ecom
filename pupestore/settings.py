import os
import django_heroku
from dotenv import load_dotenv
load_dotenv()

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv('DEBUG')
DEBUG = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', 'django-ecommerce-pupestore.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Custom apps for project
    'storemain.apps.StoremainConfig',
    'checkout.apps.CheckoutConfig',
    'orders.apps.OrdersConfig',
    'products.apps.ProductsConfig',
    'customers.apps.CustomersConfig',
    # Others
    'crispy_forms'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Whitenoise for simplified static file serving:
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'pupestore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # custom for cart count
                'pupestore.context_processors.global_context',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

CRISPY_TEMPLATE_PACK= 'bootstrap4'

WSGI_APPLICATION = 'pupestore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# PostgreSQL Elephantsql DB setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER' : os.getenv('DB_USER'),
        'PASSWORD' : os.getenv('DB_PASSWORD'),
        'HOST' : os.getenv('DB_HOST'),
    }
}

# Custom user model
# https://www.kite.com/blog/python/custom-django-user-model/
AUTH_USER_MODEL = 'storemain.User'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# https://stackoverflow.com/questions/8687927/difference-between-static-static-url-and-static-root-on-django
# https://medium.com/@vonkunesnewton/understanding-static-files-in-django-heroku-1b8d2f003977

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# The static url is the url path where a client or browser can access static files.
STATIC_URL = '/static/'

# This generates the directory where files static files are placed when you run ./manage.py collectstatic.
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = '/img/'

MEDIA_ROOT = os.path.join(BASE_DIR, "static/img")

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/customers/login'

# if DEBUG == True:
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# else:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pupestore.contact@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

FREE_DELIVERY_THRESHOLD = 30

STRIPE_CURRENCY = 'gbp'
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY','')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY','')

# Activate Django-Heroku.
django_heroku.settings(locals())