FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1  # Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1  # Ensures our console output is not buffered by Docker, but is logged directly

WORKDIR /carbon-home-watcher-django-htmx

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
