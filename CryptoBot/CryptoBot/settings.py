"""
Django settings for CryptoBot project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from pathlib import Path
import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

NGROK_HOST = env('NGROK_HOST')

ALLOWED_HOSTS = [NGROK_HOST, 'localhost', '127.0.0.1']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bot',
    'django_telegrambot',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CryptoBot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CryptoBot.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'psqlextra.backend',
        'NAME': env('PSQL_DB_NAME'),
        'USER': env('PSQL_DB_USER'),
        'HOST': env('PSQL_DB_HOST'),
        'PORT': '5454',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DJANGO_TELEGRAMBOT = {

    'MODE' : 'WEBHOOK', #(Optional [str]) # The default value is WEBHOOK,
                        # otherwise you may use 'POLLING'
                        # NB: if use polling you must provide to run
                        # a management command that starts a worker

    'WEBHOOK_SITE' : f'https://{NGROK_HOST}',
    'WEBHOOK_PREFIX' : '/crypto_bot', # (Optional[str]) # If this value is specified,
                                  # a prefix is added to webhook url

    #'WEBHOOK_CERTIFICATE' : 'cert.pem', # If your site use self-signed
                         #certificate, must be set with location of your public key
                         #certificate.(More info at https://core.telegram.org/bots/self-signed )

    'STRICT_INIT': True, # If set to True, the server will fail to start if some of the
                             # apps contain telegrambot.py files that cannot be successfully
                             # imported.

    'BOTS' : [
        {
           'TOKEN': env('BOT_TOKEN'), #Your bot token.

           #'ALLOWED_UPDATES':(Optional[list[str]]), # List the types of
                                                   #updates you want your bot to receive. For example, specify
                                                   #``["message", "edited_channel_post", "callback_query"]`` to
                                                   #only receive updates of these types. See ``telegram.Update``
                                                   #for a complete list of available update types.
                                                   #Specify an empty list to receive all updates regardless of type
                                                   #(default). If not specified, the previous setting will be used.
                                                   #Please note that this parameter doesn't affect updates created
                                                   #before the call to the setWebhook, so unwanted updates may be
                                                   #received for a short period of time.

           #'TIMEOUT':(Optional[int|float]), # If this value is specified,
                                   #use it as the read timeout from the server

           #'WEBHOOK_MAX_CONNECTIONS':(Optional[int]), # Maximum allowed number of
                                   #simultaneous HTTPS connections to the webhook for update
                                   #delivery, 1-100. Defaults to 40. Use lower values to limit the
                                   #load on your bot's server, and higher values to increase your
                                   #bot's throughput.

           #'POLL_INTERVAL' : (Optional[float]), # Time to wait between polling updates from Telegram in
                           #seconds. Default is 0.0

           #'POLL_CLEAN':(Optional[bool]), # Whether to clean any pending updates on Telegram servers before
                                   #actually starting to poll. Default is False.

           #'POLL_BOOTSTRAP_RETRIES':(Optional[int]), # Whether the bootstrapping phase of the `Updater`
                                   #will retry on failures on the Telegram server.
                                   #|   < 0 - retry indefinitely
                                   #|     0 - no retries (default)
                                   #|   > 0 - retry up to X times

           #'POLL_READ_LATENCY':(Optional[float|int]), # Grace time in seconds for receiving the reply from
                                   #server. Will be added to the `timeout` value and used as the read timeout from
                           #server (Default: 2).
        },
        #Other bots here with same structure.
    ],

}
