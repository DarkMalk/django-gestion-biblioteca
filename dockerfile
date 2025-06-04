FROM python:3.12-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
  default-libmysqlclient-dev build-essential pkg-config cron

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN pip install gunicorn

# Create a static files directory
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate

# Command for running cron jobs
RUN python manage.py crontab add

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gestion_biblioteca.wsgi:application"]