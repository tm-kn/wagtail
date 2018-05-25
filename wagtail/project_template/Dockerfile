FROM python:3.6
LABEL maintainer="hello@wagtail.io"

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    # Set PYTHONPATH to be able to use django-admin.
    PYTHONPATH=/app \
    # Use production settings by default.
    DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production

# Install gunicorn to use it as your application server.
RUN pip install "gunicorn>=19.8,<19.9"

# Install your application's requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Move your app's files.
COPY . .

# Make the app operate as a separate user rather than using the root user.
RUN useradd wagtail
RUN chown -R wagtail .
USER wagtail

# Set port Gunicorn is operating on and Docker is exposing.
ENV PORT 8000
EXPOSE 8000

# Set number of Gunicorn workers.
ENV WEB_CONCURRENCY 3

# Collect static files.
RUN SECRET_KEY=none django-admin collectstatic --noinput --clear

# Migrate database and start gunicorn when container starts.
CMD sh -xec "django-admin migrate --noinput &&\
             gunicorn {{ project_name }}.wsgi:application"
