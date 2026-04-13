FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

COPY backend/ /app/
COPY frontend/ /frontend/

WORKDIR /frontend
RUN npm install && npm run build

RUN mkdir -p /app/static/
RUN cp -r /frontend/build/* /app/static/

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    gunicorn kittygram_backend.wsgi:application --bind 0.0.0.0:8000