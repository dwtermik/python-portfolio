# shopping_list.py
def show_menu():
    print("\nМеню:")
    print("1. Добавить продукт")
    print("2. Удалить продукт")
    print("3. Показать список")
    print("4. Выход")

def add_item(shopping_list):
    item = input("Введите название продукта: ").strip()
    if item:
        shopping_list.append(item)
        print(f"Продукт '{item}' добавлен!")
    else:
        print("Ошибка: введите название продукта!")

def remove_item(shopping_list):
    if not shopping_list:
        print("Список пуст!")
        return
    show_list(shopping_list)
    try:
        index = int(input("Введите номер продукта для удаления: ")) - 1
        if 0 <= index < len(shopping_list):
            removed = shopping_list.pop(index)
            print(f"Продукт '{removed}' удалён!")
        else:
            print("Ошибка: неверный номер!")
    except ValueError:
        print("Ошибка: введите число!")

def show_list(shopping_list):
    if not shopping_list:
        print("Список покупок пуст!")
    else:
        print("\nСписок покупок:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

def main():
    shopping_list = []
    while True:
        show_menu()
        choice = input("Выберите действие (1-4): ").strip()
        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            show_list(shopping_list)
        elif choice == "4":
            print("Пока, бро!")
            break
        else:
            print("Ошибка: выберите 1, 2, 3 или 4!")

if __name__ == "__main__":
    main()