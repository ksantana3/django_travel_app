# Travel Buddy

A small travel planner I built with Django while learning full-stack web development. Users register, log in, post upcoming trips, and join trips that other users have posted.

> **Status:** Archived portfolio project — not maintained; dependencies are outdated and it is not intended for deployment.

More of my work: [kylesantana.com](https://kylesantana.com)

## Features

- Registration and login with server-side validation (name, username, password length, password confirmation, duplicate usernames)
- Passwords hashed with bcrypt
- Session-based authentication
- Dashboard listing the trips you've joined and other users' trips you can join
- Add a trip (destination, description, start/end dates) with validation: dates required, start date in the future, end date after start date
- Trip detail page showing who planned the trip and who else is going
- Data model: one-to-many (a user creates many trips) and many-to-many (users join many trips)

## Tech stack

Versions are as pinned in `requirements.txt`:

- Python 3.6 (what the project was originally run with)
- Django 2.2.1
- bcrypt 3.1.6
- SQLite (Django's default database backend)
- Bootstrap 4.3.1 (loaded from a CDN in the templates)

## Running it locally

These pinned versions are old, so use a Python version they install cleanly on (Python 3.6–3.8 is the safest bet).

```bash
git clone https://github.com/ksantana3/django_travel_app.git
cd django_travel_app

python -m venv venv
# Windows: venv\Scripts\activate
source venv/bin/activate

pip install -r requirements.txt
```

### Environment variables

Settings are read from environment variables in `travel_buddy/settings.py`:

| Variable | Default | Notes |
| --- | --- | --- |
| `DJANGO_DEBUG` | `False` | Set to `True` for local development. |
| `DJANGO_SECRET_KEY` | none | Required when `DJANGO_DEBUG` is not `True`. With debug on and no key set, a random throwaway key is generated at startup (sessions won't survive a restart). |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated list of hostnames. |

For local development the simplest setup is:

```bash
# macOS / Linux
export DJANGO_DEBUG=True

# Windows PowerShell
$env:DJANGO_DEBUG = "True"
```

To use a fixed key instead, generate one and set `DJANGO_SECRET_KEY`:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Database and server

The SQLite database is not checked in, so create it from the migrations:

```bash
python manage.py migrate
python manage.py runserver
```

Then open http://localhost:8000/ to register and log in.

## Project structure

```
django_travel_app/
├── manage.py
├── requirements.txt
├── travel_buddy/            # Project settings, root URLconf, WSGI entry point
└── apps/
    ├── logreg/              # Registration, login, logout
    │   ├── models.py        # User model + validation (UserManager)
    │   ├── views.py
    │   ├── urls.py
    │   ├── migrations/
    │   └── templates/logreg/
    └── travel_app/          # Trips: dashboard, add, detail, join
        ├── models.py        # Trip model + validation (tripManager)
        ├── views.py
        ├── urls.py
        ├── migrations/
        └── templates/travel_app/
```

Routes:

| Path | Purpose |
| --- | --- |
| `/` | Login and registration page |
| `/register`, `/login`, `/logout` | Auth actions |
| `/travel/` | Dashboard |
| `/travel/add` | New trip form |
| `/travel/destination/<id>` | Trip details |
| `/travel/join/<id>` | Join a trip |

## Notes

This was a learning project, so there are rough edges I've left as they were: for example, the trip pages error out instead of redirecting to the login page if you aren't signed in, and the templates reference a stylesheet (`login/css/styles.css`) that isn't in the repo.
