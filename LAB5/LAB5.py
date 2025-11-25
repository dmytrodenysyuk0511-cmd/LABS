"""
Лабораторна робота №5
Тема: Робота з бібліотеками та virtualenv
"""

# --- 1. Імпорт 10 різних бібліотек ---
import requests         # Для HTTP запитів
import numpy as np      # Для роботи з масивами
import pandas as as_pd  # Для роботи з табличними даними
import matplotlib.pyplot as plt # Для графіків
from PIL import Image   # (Pillow) Для обробки зображень
from bs4 import BeautifulSoup # Для парсингу HTML
from dotenv import load_dotenv # Для змінних оточення
import colorama         # Для кольорового тексту в консолі
import emoji            # Для емодзі
import yaml             # (PyYAML) Для роботи з YAML файлами

# Ініціалізація colorama для коректного відображення кольорів
colorama.init()

print("Всі бібліотеки успішно імпортовані.\n")

# --- 2. Використання 5 бібліотек у блоках try-except ---

# Блок 1: Requests (Отримання статусу сайту)
print(f"{colorama.Fore.CYAN}--- Блок 1: Requests ---{colorama.Style.RESET_ALL}")
try:
    response = requests.get('https://www.google.com')
    print(f"Статус код відповіді від Google: {response.status_code}")
    if response.status_code == 200:
        print("Сайт доступний.")
except Exception as e:
    print(f"Помилка в блоці Requests: {e}")


# Блок 2: Numpy (Створення масиву)
print(f"\n{colorama.Fore.CYAN}--- Блок 2: Numpy ---{colorama.Style.RESET_ALL}")
try:
    arr = np.array([1, 2, 3, 4, 5])
    squared_arr = arr ** 2
    print(f"Оригінальний масив: {arr}")
    print(f"Квадрати елементів: {squared_arr}")
except Exception as e:
    print(f"Помилка в блоці Numpy: {e}")


# Блок 3: Pandas (Створення простого DataFrame)
print(f"\n{colorama.Fore.CYAN}--- Блок 3: Pandas ---{colorama.Style.RESET_ALL}")
try:
    data = {
        'Ім\'я': ['Анна', 'Богдан', 'Вікторія'],
        'Вік': [20, 21, 19]
    }
    df = as_pd.DataFrame(data)
    print("Створена таблиця Pandas:")
    print(df)
except Exception as e:
    print(f"Помилка в блоці Pandas: {e}")


# Блок 4: Matplotlib (Створення простого графіка без відображення вікна)
print(f"\n{colorama.Fore.CYAN}--- Блок 4: Matplotlib ---{colorama.Style.RESET_ALL}")
try:
    x = [1, 2, 3, 4]
    y = [10, 20, 25, 30]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    print("Графік успішно згенеровано (в пам'яті), об'єкт:", ax)
    # plt.show() # Закоментовано, щоб не зупиняти виконання скрипта
except Exception as e:
    print(f"Помилка в блоці Matplotlib: {e}")


# Блок 5: Emoji (Вивід емодзі)
print(f"\n{colorama.Fore.CYAN}--- Блок 5: Emoji ---{colorama.Style.RESET_ALL}")
try:
    print(emoji.emojize('Python is :thumbs_up:'))
    print(emoji.emojize('Laboratorna robota is done :check_mark_button:'))
except Exception as e:
    print(f"Помилка в блоці Emoji: {e}")

print(f"\n{colorama.Back.GREEN}{colorama.Fore.BLACK} Роботу завершено! {colorama.Style.RESET_ALL}")