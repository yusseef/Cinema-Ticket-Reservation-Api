
# Cinema Ticket RservationAPI

API for Cinema ticket reservation made by Django, DjangoREST.
- FBV apiview
- CBV APIVIEW
- Generics
- Viewsets

## Features

- Add guests
- Add movies
- Add halls
- Book a reservation to a guest by selecting a movie.
- JWT authentication for booking a ticket or editing (Movies, Halls).

## Acknowledgements
 - [Python](https://www.python.org/)
 - [Django](https://www.djangoproject.com/)
 - [DjangoREST](https://www.django-rest-framework.org/)
 - [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)


## Installation

After you clone the repo run the following commands

```bash
  python -m venv venv
  python pip install -r requirments.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```
And you good to go.

### All Apis Routes documented in the follwoing route by swagger:


```http
   /swagger
```
## Feedback

If you have any feedback, please reach out to me at yussef.raouf11@gmail.com


![Logo](http://ForTheBadge.com/images/badges/made-with-python.svg)
![Logo](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

