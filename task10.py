# Inventory Manager Using OOP, Lambda, and Comprehensions
import random

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_days):
        super().__init__(name, price, quantity)
        self.expiry_days = expiry_days

    def total_value(self):
        value = super().total_value()
        if self.expiry_days < 5:
            value *= 0.8  # 20% discount
        return value

class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_inventory(self):
        print("\nInventory List:")
        for idx, product in enumerate(self.products, 1):
            if isinstance(product, PerishableProduct):
                print(f"{idx}. {product.name} (Perishable) - Price: {product.price}, Qty: {product.quantity}, Expiry: {product.expiry_days} days, Total Value: {product.total_value():.2f}")
            else:
                print(f"{idx}. {product.name} - Price: {product.price}, Qty: {product.quantity}, Total Value: {product.total_value():.2f}")

    def search_by_name(self, term):
        term = term.lower()
        results = list(filter(lambda p: term in p.name.lower(), self.products))
        print(f"\nSearch results for '{term}':")
        for idx, product in enumerate(results, 1):
            print(f"{idx}. {product.name} - Qty: {product.quantity}")

    def restock_all(self):
        for product in self.products:
            added = random.randint(1, 10)
            product.quantity += added
        print("All products restocked.")

    def export_summary(self, filename="inventory_summary.txt"):
        summary = {
            product.name: {
                "total_value": product.total_value(),
                "quantity": product.quantity
            }
            for product in self.products
        }
        with open(filename, "w") as f:
            for name, info in summary.items():
                f.write(f"{name}: Quantity={info['quantity']}, Total Value={info['total_value']:.2f}\n")
        print(f"Inventory summary exported to {filename}")

if __name__ == "__main__":
    manager = InventoryManager()
    manager.add_product(Product("Soap", 50, 10))
    manager.add_product(PerishableProduct("Milk", 100, 5, 3))
    manager.add_product(PerishableProduct("Cheese", 200,2,10))

    manager.list_inventory()
    manager.search_by_name("milk")
    manager.restock_all()
    manager.list_inventory()
    manager.export_summary()