class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item: Product):
        self.items.append(item)
    
    def get_high_price_items(self) -> HighValueIterator:
        return HighValueIterator(self.items)

class HighValueIterator:
    def __init__(self, products: list[Product]):
        self.products = products
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self) -> Product:
        while self.index < len(self.products):
            result = self.products[self.index]
            self.index += 1
            if result.price >= 500:
                return result
        raise StopIteration

def main():
    print("[Main] Starting the program")
    shopping_cart = ShoppingCart()
    shopping_cart.add_item(Product("Laptop", 1000))
    shopping_cart.add_item(Product("Phone", 500))
    shopping_cart.add_item(Product("Tablet", 300))
    print("[Main] Scanning the shopping cart to find products with price >= $500")
    high_value_items = shopping_cart.get_high_price_items()
    for item in high_value_items:
        print(f"[Main] Item: {item.name}, Price: {item.price}")
    print("[Main] Program ended")

if __name__ == "__main__":
    main()