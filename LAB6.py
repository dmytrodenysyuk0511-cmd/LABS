import json
import os
from datetime import datetime
from functools import wraps


def log_to_json(filename="log_data.json"):
    """
    Декоратор, який логує аргументи та результат виконання функції у JSON-файл.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Виконання оригінальної функції
            result = func(*args, **kwargs)

            # Формування запису для логу
            log_entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "function_name": func.__name__,
                "arguments": args,
                "keyword_arguments": kwargs,
                "return_value": result
            }

            # Читання існуючого файлу або створення нового списку
            data = []
            if os.path.exists(filename) and os.path.getsize(filename) > 0:
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # Перевірка, чи зчитані дані є списком
                        if not isinstance(data, list):
                            data = []
                except json.JSONDecodeError:
                    data = []

            # Додавання нового запису
            data.append(log_entry)

            # Запис оновленого списку назад у файл
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            return result

        return wrapper

    return decorator