import os
from pathlib import Path
from configurations import Configuration
from configurations import values
from dotenv import load_dotenv
from corsheaders.defaults import default_headers
from corsheaders.defaults import default_methods
import cloudinary
import cloudinary.uploader
import cloudinary.api

load_dotenv()


class Dev(Configuration):
    BASE_DIR = Path(__file__).resolve().parent.parent

    SECRET_KEY = values.SecretValue()

    DEBUG = True

    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(";")

    CORS_ALLOW_HEADERS = list(default_headers)

    CORS_ALLOW_METHODS = list(default_methods)

    # CORS_ALLOW_ALL_ORIGINS = True

    CORS_ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(";")

    CSRF_TRUSTED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(";")

    SITE_ID = 1

    AUTH_USER_MODEL = "custom_user.User"

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.sites",
        "django.contrib.staticfiles",
        "corsheaders",
        "rest_framework",
        "phonenumber_field",
        "v1",
        "custom_user",
        "taxation",
    ]

    cloudinary.config(
        cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
        api_key=os.getenv("CLOUDINARY_API_KEY"),
        api_secret=os.getenv("CLOUDINARY_API_SECRET"),
        secure=os.getenv("CLOUDINARY_SECURE"),
    )

    MIDDLEWARE = [
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "core.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "core.wsgi.application"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
            "PORT": os.getenv("DATABASE_PORT"),
        }
    }

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_TZ = True

    STATIC_URL = "static/"

    STATIC_ROOT = BASE_DIR / "staticfiles"

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    REST_FRAMEWORK = {
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.IsAuthenticated",
        ],
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication",
        ],
        "DEFAULT_RENDERER_CLASSES": [
            "rest_framework.renderers.JSONRenderer",
        ],
        "DEFAULT_PARSER_CLASSES": [
            "rest_framework.parsers.JSONParser",
            "rest_framework.parsers.FormParser",
            "rest_framework.parsers.MultiPartParser",
        ],
        "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 20,
        "TEST_REQUEST_DEFAULT_FORMAT": "json",
        "DEFAULT_THROTTLE_CLASSES": [
            "rest_framework.throttling.ScopedRateThrottle",
        ],
    }

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "[{asctime}s] PID: {process:d} [{levelname}s] {message}s",
                "style": "{",
            },
            "simple": {
                "format": "[{asctime}s] PID: {process:d} [{levelname}s] {message}s",
                "style": "{",
            },
        },
        "handlers": {
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "filename": os.getenv("DJANGO_LOG_PATH"),
            },
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": os.getenv("DJANGO_LOG_LEVEL").upper(),
                "propagate": True,
                "formatter": "verbose",
            },
            "django.db.backends": {
                "handlers": ["console"],
                "level": "INFO",
            },
        },
    }

    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    MEDIA_URL = "/media/"


class Prod(Dev):
    DEBUG = False

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "[{asctime}s] PID: {process:d} [{levelname}s] {message}s",
                "style": "{",
            },
            "simple": {
                "format": "[{asctime}s] PID: {process:d} [{levelname}s] {message}s",
                "style": "{",
            },
        },
        "handlers": {
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "filename": os.getenv("DJANGO_LOG_PATH"),
            },
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["file"],
                "level": os.getenv("DJANGO_LOG_LEVEL").upper(),
                "propagate": True,
                "formatter": "verbose",
            },
        },
    }
