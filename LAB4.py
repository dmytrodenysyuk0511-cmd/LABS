def format_price(price):
    """Форматує ціну з двома знаками після коми"""
    return "Ціна: " + str(round(price, 2)) + " грн"


def check_availability(*product_names):
    """Перевіряє наявність товарів у магазині"""
    store = {
        "яблуко": True,
        "банан": False,
        "молоко": True,
        "хліб": True,
        "сир": False
    }
    availability = {}
    for product in product_names:
        availability[product] = store.get(product, False)
    return availability


def make_order(order_list):
    """Оформляє замовлення і підраховує загальну вартість"""
    price_list = {
        "яблуко": 25.5,
        "банан": 30,
        "молоко": 45,
        "хліб": 20,
        "сир": 80
    }

    availability = check_availability(*order_list)
    if not all(availability.values()):
        print("Немає в наявності:")
        for product, is_available in availability.items():
            if not is_available:
                print("-", product)
        return

    total_price = sum(price_list[product] for product in order_list)
    print("Замовлення прийнято,", format_price(total_price))


# --- ТОЧКА ВХОДУ ---
def main():
    user_action = input("Введіть дію (1 - показати ціни, 2 - купити): ")

    if user_action == "1":
        price_list = {
            "яблуко": 25.5,
            "банан": 30,
            "молоко": 45,
            "хліб": 20,
            "сир": 80
        }
        for product_name, price in price_list.items():
            print(product_name, "-", format_price(price))

    elif user_action == "2":
        raw_input = input("Введіть товари через кому: ").lower().split(",")
        order_list = [item.strip() for item in raw_input]
        make_order(order_list)

    else:
        print("Невірна дія")


# Запуск тільки якщо файл є основним
if name == "main":
    main()