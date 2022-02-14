# point-of-sale

## Generating the secret key for Django:
Open a terminal and execute:
```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
Grab the output and replace the <SECRET_KEY> on the template below.

## Creating .key file
Create a `.env` file in the same directory of `manage.py` file using this template:

```
SECRET_KEY=<SECRET_KEY>
DEBUG=True
ALLOWED_HOSTS=.localhost,127.0.0.1
DATABASE_NAME=<DATABASE_NAME>
DATABASE_USER=<DATABASE_USER>
DATABASE_PASSWORD=<DATABASE_PASSWORD>
DATABASE_HOST=<DATABASE_HOST>
DATABASE_PORT=<DATABASE_PORT>
```
