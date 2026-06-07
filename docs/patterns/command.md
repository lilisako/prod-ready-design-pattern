# Command Pattern

Command Pattern is a behavioral design pattern that allows you to encapsulate a request as an object, which can be parameterized and passed to other objects. This pattern is useful when you want to parameterize methods with different arguments. 

For example, you have a shopping cart and you want to allow the user to add an item to the cart, undo the last action etc. When the last action is adding an item to the cart and you want to undo it, you need to remove the item from the cart. With Command pattern, you can easily add a new command without changing the existing code. Also when you call undo, you don't need to know the details of the command. You just need to call the undo method of the command.


```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item: str):
        self.items.append(item)
    
    def remove_item(self, item: str):
        self.items.remove(item)
    
    
class Command:
    def execute(self) -> None:
        pass 
    
    def undo(self) -> None:
        pass

class AddItemCommand(Command):
    def __init__(self, shopping_cart: ShoppingCart, item: str):
        self.shopping_cart = shopping_cart
        self.item = item
    
    def execute(self) -> None:
        self.shopping_cart.add_item(self.item)
        print(f"[AddItemCommand] Added item: {self.item}")
    
    def undo(self) -> None:
        self.shopping_cart.remove_item(self.item)
        print(f"[AddItemCommand] Removed item: {self.item}")

class CartHistoryManager:
    def __init__(self):
        self.history = []
    
    def add_command(self, command: Command):
        command.execute()
        self.history.append(command)
    
    def undo_last_command(self):
        if self.history:
            self.history.pop().undo()
        else:
            print("[CartHistoryManager] No commands to undo")
 
print("[Main] Starting the program")
shopping_cart = ShoppingCart()
cart_history_manager = CartHistoryManager()
cart_history_manager.add_command(AddItemCommand(shopping_cart, "Laptop"))
cart_history_manager.add_command(AddItemCommand(shopping_cart, "Keyboard"))
cart_history_manager.add_command(AddItemCommand(shopping_cart, "Monitor"))
cart_history_manager.undo_last_command()
print(f"[Main] Shopping cart items: {shopping_cart.items}")
print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[AddItemCommand] Added item: Laptop
[AddItemCommand] Added item: Keyboard
[AddItemCommand] Added item: Monitor
[AddItemCommand] Removed item: Monitor
[Main] Shopping cart items: ['Laptop', 'Keyboard']
[Main] Program ended
```
