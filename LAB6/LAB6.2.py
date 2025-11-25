from LAB6 import (log_to_json)


# Застосування декоратора з вказанням імені файлу для логів
@log_to_json("lab6_logs.json")
def calculate_area(width, height):
    return width * height


@log_to_json("lab6_logs.json")
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    # Виклики функцій для тестування
    print("Обчислення площі:", calculate_area(10, 5))
    print("Привітання:", greet_user("Саня", greeting="Привіт"))

    print("\nДані успішно записані у файл lab6_logs.json")