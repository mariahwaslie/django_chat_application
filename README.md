# Django Chat Application

A Django chat application with user registration, login, profiles, chat group creation, and real-time group chat over WebSockets.

The main project package is `pro1`, with separate apps for accounts and chat.

## Features

- Home page using a shared Bootstrap-based base template
- User registration with username, email, and password fields
- User login and profile page
- Chat group model with unique names, descriptions, and slug-based room URLs
- Group listing page with links to join rooms
- Chat room page with a message log and send box
- WebSocket chat powered by Django Channels
- Redis-backed channel layer configured for live room broadcasts
- SQLite database for local development

## Project Structure

```text
.
├── README.md
├── requirements.txt
├── manage.py
├── db.sqlite3
├── account/
│   ├── forms.py
│   ├── urls.py
│   ├── views.py
│   └── templates/account/
├── chat2/
│   ├── consumers.py
│   ├── forms.py
│   ├── models.py
│   ├── routing.py
│   ├── urls.py
│   ├── views.py
│   └── templates/chat/
├── pro1/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── static/css/
└── templates/
```

## Apps

### `account`

Handles authentication-related pages:

- `accounts/register/` - create a new account
- `accounts/login/` - log in
- `accounts/profile/` - view the logged-in user's profile

### `chat2`

Handles chat groups and chat rooms:

- `chat/` - chat index view
- `chat/<room_name>/` - individual chat room
- group creation view
- group listing/join view
- WebSocket route: `ws/chat/<room_name>/`

### `pro1`

Contains the project settings, root URL routing, ASGI configuration, and home page view.

## Requirements

A `requirements.txt` file is included with the Python packages needed by the app:

```text
Django==5.0.4
channels>=4.0,<5.0
daphne>=4.0,<5.0
channels-redis>=4.0,<5.0
django-bootstrap5>=24.0,<26.0
django-braces>=1.15,<2.0
```

Redis is also required because `CHANNEL_LAYERS` is configured to use `channels_redis` at `localhost:6379`.

## Setup

From this folder:

### macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

Install Redis with Homebrew if you do not already have it:

```bash
brew install redis
```

Start Redis in another terminal before using the live chat features:

```bash
redis-server
```

Then start the Django development server:

```bash
python manage.py runserver
```

Open the app at:

```text
http://127.0.0.1:8000/
```

### Windows / PC

From this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

Redis is required for live chat. On Windows, a common option is to run Redis through Docker Desktop:

```powershell
docker run --name redis-chat -p 6379:6379 redis
```

If you already have Redis installed another way, make sure it is running on:

```text
localhost:6379
```

Then start the Django development server:

```powershell
python manage.py runserver
```

Open the app at:

```text
http://127.0.0.1:8000/
```

## Common Commands

Run database migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Run tests:

```bash
python manage.py test
```

## How Chat Works

The room page opens a WebSocket connection to:

```text
ws://<host>/ws/chat/<room_name>/
```

`chat2.consumers.ChatConsumer` joins a Channels group named after the room, receives JSON messages containing a `message` and `username`, broadcasts them to everyone in the same room, and appends received messages to the chat log in the browser.

## Notes

- The local database file `db.sqlite3` is included in the project directory.
- Static CSS files live in `django_chat_application/static/css/`.
- The app uses Bootstrap 5 from a CDN and `django-bootstrap5` template tags for forms.
- The project is configured with `DEBUG = True` and an in-code secret key, so it is intended for local development only unless production settings are added.
