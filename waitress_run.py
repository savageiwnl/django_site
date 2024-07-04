import os
import django
from django.core.wsgi import get_wsgi_application
from waitress import serve

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Настраиваем Django
django.setup(set_prefix=False)

# Получаем WSGI-приложение Django
application = get_wsgi_application()

if __name__ == "__main__":
    # Запускаем сервер Waitress
    serve(application, host='0.0.0.0', port=8000)
