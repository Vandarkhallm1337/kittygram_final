FROM python:3.11-slim

WORKDIR /app

# системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# копируем backend
COPY backend/ /app/

# копируем frontend
COPY frontend/ /frontend/

# собираем фронт
WORKDIR /frontend
RUN npm install && npm run build

# переносим build в Django
RUN mkdir -p /app/static/
RUN cp -r /frontend/build /app/

# обратно в backend
WORKDIR /app

# зависимости python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# запуск
CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    gunicorn kittygram_backend.wsgi:application --bind 0.0.0.0:$PORT