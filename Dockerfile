FROM python:3.11

RUN mkdir 'store'

WORKDIR /store

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY . .

CMD poetry run python manage.py migrate && poetry run gunicorn -w=4 --bind 0.0.0.0:8000 store.wsgi
