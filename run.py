#!/usr/bin/env python3

from facefusion import core
from pyngrok import ngrok
import time

if __name__ == '__main__':
    # Запуск вашего приложения
    get_ipython().system_raw('python run.py &')

    # Создание туннеля
    public_url = ngrok.connect(port='5000')  # Укажите порт вашего приложения
    print(f"Your application is running publicly at: {public_url}")

    # Ожидание, чтобы приложение продолжало работать
    while True:
        time.sleep(1)