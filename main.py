from Menu import Menu
from utils import save_menu, load_menu

def main():
    restaurant_name = input("Enter the restaurant name: ")
    waiter_percentage = float(input("Enter the waiter percentage: "))

    menu = Menu(restaurant_name, waiter_percentage)
    menu.menu = load_menu()

    while True:
        print("\n1. Add Item\n2. Remove Item\n3. Update Item\n4. Search Item\n5. List Items\n6. Checkout\n7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category: ")
            item = input("Enter item: ")
            product = input("Enter product: ")
            price = float(input("Enter price: "))
            menu.add_item(category, item, product, price)
            save_menu(menu.menu)

        elif choice == '2':
            category = input("Enter category: ")
            item = input("Enter item: ")
            product = input("Enter product: ")
            menu.remove_item(category, item, product)
            save_menu(menu.menu)

        elif choice == '3':
            category = input("Enter category: ")
            item = input("Enter item: ")
            product = input("Enter product: ")
            new_price = float(input("Enter new price: "))
            menu.update_item(category, item, product, new_price)
            save_menu(menu.menu)

        elif choice == '4':
            search_term = input("Enter search term: ")
            results = menu.search_item(search_term)
            for result in results:
                print(f"Category: {result[0]}, Item: {result[1]}, Product: {result[2]}, Price: {result[3]}")

        elif choice == '5':
            items = menu.list_items()
            for category, item_dict in items.items():
                print(f"\nCategory: {category}")
                for item, products in item_dict.items():
                    print(f" Item: {item}")
                    for product, price in products.items():
                        print(f" Product: {product} - Price: {price}")

        elif choice == '6':
            selected_items = []
            while True:
                category = input("Enter category (or 'done' to finish): ")
                if category.lower() == 'done':
                    break
                item = input("Enter item: ")
                product = input("Enter product: ")
                price = float(input("Enter price: "))
                selected_items.append((category, item, product, price))
            total = menu.calculate_total(selected_items)
            print(f"Total to pay: {total}")

        elif choice == '7':
            break

if __name__ == "__main__":
    main()
    