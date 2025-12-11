def format_price(price): #Функція1 - формат ціни
    return f"{price:.2f} грн"

def check_availability(store, *items): #Функція2 - чек наявності
    return {item: (item in store and store[item][1]) for item in items}

def order(store): #Функція3 - замовлення
    order = input("Введіть товари через пробіл: ").split()
    check = check_availability(store, *order)

    unavailable = [item for item, available in check.items() if not available]

    if unavailable:
        print("Замовлення скасовано! Немає:", ", ".join(unavailable)) #join обєднує в рядок через ", "
        return

    total = 0
    print("Замовлення:")
    for item in order:
        price = store[item][0]
        print(f"{item}: {format_price(price)}")
        total += price
    print("Загалом:", format_price(total))

def main():
    store = {"Стіл": [1499.99, True],
            "Стілець": [500.50, False],
            "Лампа": [400.50, False],
            "Шафа": [3199.99, True],
            "Диван": [5800.25, True]}

    while True:
        choice = input("Оберіть дію (1 - Купити, 2 - Переглянути ціни):")
        if choice == "1":
            order(store)
        elif choice == "2":
            for item, (price, available) in store.items():
                status = "+" if available else "-"
                print(f"{item}: {format_price(price)} ({status})")
        else:
            print("Непрописаний варіант!")

if __name__ == '__main__':
    main()
