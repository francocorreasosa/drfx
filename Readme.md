# DRFx

A framework for launching new Django Rest Framework projects quickly. Comes with a custom user model, login/logout/signup, social authentication via django-allauth, and more.

## Features

- Django 3.1, Django REST Framework 3.13, and Python 3.10
- Custom user model
- Token-based auth
- Signup/login/logout
- [django-allauth](https://github.com/pennersr/django-allauth) for social auth
- [Poetry](https://python-poetry.org/) for virtualenvs

## First-time setup

1.  Make sure Python 3.7x and Poetry are already installed.
2.  Clone the repo and configure the virtual environment:

```
$ git clone https://github.com/francocorreasosa/drfx.git
$ cd drfx
$ poetry install
```

3.  Set up the initial migration for our custom user models in users and build the database.

```
(drfx) $ poetry run ./manage.py makemigrations users
(drfx) $ poetry run ./manage.py migrate
(drfx) $ poetry run ./manage.py createsuperuser
(drfx) $ poetry run ./manage.py runserver
```

4.  Endpoints

Login with your superuser account. Then navigate to all users. Logout. Sign up for a new account and repeat the login, users, logout flow.

- login - http://127.0.0.1:8000/api/v1/rest-auth/login/
- all users - http://127.0.0.1:8000/api/v1/users
- logout - http://127.0.0.1:8000/api/v1/rest-auth/logout/
- signup - http://127.0.0.1:8000/api/v1/rest-auth/registration/
