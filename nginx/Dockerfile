FROM nginx:1.22.1
COPY nginx.conf /etc/nginx/templates/default.conf.template

# 🔥 ВАЖНО: копируем билд фронта напрямую
COPY ../frontend/build /static/