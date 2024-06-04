class Menu:
    def __init__(self, restaurant_name, waiter_percentage):
        self.restaurant_name = restaurant_name
        self.waiter_percentage = waiter_percentage
        self.menu = {}

    def add_item(self, category, item, product, price):
        if category not in self.menu:
            self.menu[category] = {}
        if item not in self.menu[category]:
            self.menu[category][item] = {}
        self.menu[category][item][product] = price

    def remove_item(self, category, item, product):
        if category in self.menu and item in self.menu[category] and product in self.menu[category][item]:
            del self.menu[category][item][product]
            if not self.menu[category][item]:
                del self.menu[category][item]
            if not self.menu[category]:
                del self.menu[category]

    def update_item(self, category, item, product, new_price):
        if category in self.menu and item in self.menu[category] and product in self.menu[category][item]:
            self.menu[category][item][product] = new_price

    def search_item(self, search_term):
        results = []
        for category, items in self.menu.items():
            for item, products in items.items():
                for product, price in products.items():
                    if search_term.lower() in product.lower():
                        results.append((category, item, product, price))
        return results

    def list_items(self):
        return self.menu

    def calculate_total(self, selected_items):
        total = sum([price for category, item, product, price in selected_items])
        return total