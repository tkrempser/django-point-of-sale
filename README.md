# django-point-of-sale

## Live demo
Browsable REST API endpoint: https://pos.krempser.com.br/. Also available in raw json: https://pos.krempser.com.br/.json.

## Class diagrams
Basic representation of this project's models:
![Class diagram](https://raw.githubusercontent.com/tkrempser/point-of-sale/main/etc/class-diagram.svg)

## API Endpoints
| Path | Description | Verbs |
| --- | --- | --- |
| /customers/ | Read, create, update, delete customers | GET, POST, PUT, DELETE |
| /orders/ | Read, create, update, delete orders | GET, POST, PUT, DELETE |
| /order-products/ | Read, create, update, delete products from orders | GET, POST, PUT, DELETE |
| /products/ | Read, create, update, delete products | GET, POST, PUT, DELETE |
| /users/ | Read, create, update, delete sellers | GET, POST, PUT, DELETE |
| /users/commissions/ | Read seller's commissions | GET |

## Generating the secret key for Django
Open a terminal and execute:
```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
Grab the output and replace `<SECRET_KEY>` in the template in the next section.

## Creating environment file
Create a .env file in the same directory of `manage.py` file using the template below. Replace `<SECRET_KEY>`, `<DATABASE_NAME>`, `<DATABASE_PASSWORD>`, `<DATABASE_HOST>` with your own values.

```
SECRET_KEY=<SECRET_KEY>
DEBUG=True
ALLOWED_HOSTS=.localhost,127.0.0.1
DATABASE_NAME=<DATABASE_NAME>
DATABASE_USER=postgres
DATABASE_PASSWORD=<DATABASE_PASSWORD>
DATABASE_HOST=<DATABASE_HOST>
DATABASE_PORT=5432
```

## Running a Docker PostgreSQL instance
Create a folder to store PostgreSQL data:
```
mkdir ${HOME}/postgres-data/
```
Pull PostgreSQL from Docker Hub:
```
sudo docker pull postgres
```
Create a container named `postgres`:
```
sudo docker run -d --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=<DATABASE_PASSWORD> -v ${HOME}/postgres-data/:/var/lib/postgresql/data postgres
```
Finally, start the container:
```
sudo docker start postgres
```

## Creating a user for Django administration
In the same directory of `manage.py`, execute:
```
python manage.py createsuperuser
```

## Trusted origin and CORS
In the project `settings.py` file, update the `CSRF_TRUSTED_ORIGINS` and `CORS_ALLOWED_ORIGINS` variables according to your environment.

## Runing tests
In the same directory of `manage.py`, execute:
```
pytest
```
