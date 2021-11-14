"""
Django settings for django_site project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#lk9sfvhyf6d40qlh&3)a$3kn0m$rd0&_l9qh(c##zug&1_a=r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks'
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

ROOT_URLCONF = 'django_site.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'django_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'stuDB.sqlite3',
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

# Setting LOGO
SIMPLEUI_LOGO = 'https://www.must.edu.mo/images/logo_new.png'

# Customize menu
SIMPLEUI_CONFIG = {
    'menu_display': ['Control Panel','Task Management', 'Authentication'],

    'dynamic': False,
    'menus': [
        {
            'name': 'Control Panel',
            'icon': 'fa fa-eye',
            'models': [
                {
                    'name': 'Sign-In Records',
                    'icon': 'fa fa-check-square',
                    'url': '/tasks/sign_in_records'
                },
                {
                    'name': 'Retroactive Records',
                    'icon': '',
                    'url': '/admin/tasks/signin/'
                }
            ]
            # 'url': '/tasks/dashboard/'
        },
        {
            'app': 'auth',
            'name': 'Authentication',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': 'User list',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': 'User Group',
                    'icon': 'fa fa-th-list',
                    'url': 'auth/group/'
                }
            ]
        },
        {
            'name': 'Task Management',
            'icon': 'fa fa-th-list',
            'models': [
                {
                    'name': 'SignIn',
                    # url name method :'/admin/应用名小写/模型名小写/'
                    'url': '/admin/tasks/signin/',
                    'icon': 'fa fa-tasks'
                },
                {
                    'name': 'Teacher',
                    # url name method :'/admin/应用名小写/模型名小写/'
                    'url': '/admin/tasks/teacher/',
                    'icon': 'fa fa-tasks'
                },
                {
                    'name': 'Student',
                    # url name method :'/admin/应用名小写/模型名小写/'
                    'url': '/admin/tasks/student/',
                    'icon': 'fa fa-tasks'
                },
                {
                    'name': 'Course List',
                    'url': '/admin/tasks/course',
                    'icon': 'fa fa-tasks'
                },
                {
                    'name': 'Take Course',
                    'url': '/admin/tasks/takeclass',
                    'icon': 'fa fa-tasks'
                },
                {
                    'name': 'Task list',
                    # url name method :'/admin/应用名小写/模型名小写/'
                    'url': '/admin/tasks/task/',
                    'icon': 'fa fa-tasks'
                }

            ]
        },
    ]
}

# The name actually displayed on the menu
SIMPLEUI_ICON = {
    'Task Management': 'fas fa-tasks',
    'Tasks': 'fas fa-th-list',
}

# Hide simpleui ad links and usage analysis on the right
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False

# Home page
SIMPLEUI_HOME_PAGE = ''
SIMPLEUI_HOME_TITLE = ''
SIMPLEUI_HOME_ICON = ''
