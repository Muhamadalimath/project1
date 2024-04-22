import json

# Data
def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save
def save_inventory(inventory):
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file)

# Add
def add_item(inventory):
    name = input("Введите название товара: ")
    quantity = int(input("Введите количество товара: "))
    inventory[name] = quantity
    print(f"{name} добавлен в инвентарь.")

# Count
def update_item(inventory):
    name = input("Введите название товара для изменения: ")
    if name in inventory:
        quantity = int(input("Введите новое количество товара: "))
        inventory[name] = quantity
        print(f"Количество товара {name} обновлено.")
    else:
        print("Товар не найден в инвентаре.")

# Delete
def remove_item(inventory):
    name = input("Введите название товара для удаления: ")
    if name in inventory:
        del inventory[name]
        print(f"Товар {name} удален из инвентаря.")
    else:
        print("Товар не найден в инвентаре.")

# View
def display_inventory(inventory):
    print("Текущий инвентарь:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Main
def main():
    inventory = load_inventory()

    while True:
        print("\nМеню:")
        print("1. Добавить товар")
        print("2. Изменить количество товара")
        print("3. Удалить товар")
        print("4. Просмотреть инвентарь")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            update_item(inventory)
        elif choice == '3':
            remove_item(inventory)
        elif choice == '4':
            display_inventory(inventory)
        elif choice == '5':
            save_inventory(inventory)
            print("Данные сохранены. Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main() 