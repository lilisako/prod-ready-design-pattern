# Iterator Pattern

Iterator Pattern is a behavioral design pattern that allows you to traverse a collection of objects without exposing its internal representation. For example, you have a shopping cart and you want to find all the products with price >= $500 to apply a special action. With Iterator pattern, you can easily find the products with price >= $500 without exposing the internal representation of the shopping cart. Here is an example of Iterator pattern in Python:

When you call the get_high_price_items() method, you don't need to know the details of the iterator. Even if you change the internal representation of the shopping cart (for example, from list to dictionary), you don't need to change the code of the get_high_price_items() method.

```python
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
```

Here is the output of the program:

```
[Main] Starting the program
[Main] Scanning the shopping cart to find products with price >= $500
[Main] Item: Laptop, Price: 1000
[Main] Item: Phone, Price: 500
[Main] Program ended
```
