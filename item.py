# item.py
class Item:
    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название должно быть непустой строкой!")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Цена не может быть отрицательной!")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество не может быть отрицательным!")
        self.name = name
        self.price = float(price)
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

def main():
    try:
        # Создаём товары
        bread = Item("Хлеб", 50, 2)
        milk = Item("Молоко", 100, 1)
        eggs = Item("Яйца", 70, 3)
        
        # Выводим информацию
        print(f"Товар: {bread.name}, Стоимость: {bread.total_cost()} руб.")
        print(f"Товар: {milk.name}, Стоимость: {milk.total_cost()} руб.")
        print(f"Товар: {eggs.name}, Стоимость: {eggs.total_cost()} руб.")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()