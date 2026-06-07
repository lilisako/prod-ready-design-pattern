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
 
def main():
    print("[Main] Starting the program")
    shopping_cart = ShoppingCart()
    cart_history_manager = CartHistoryManager()
    cart_history_manager.add_command(AddItemCommand(shopping_cart, "Laptop"))
    cart_history_manager.add_command(AddItemCommand(shopping_cart, "Keyboard"))
    cart_history_manager.add_command(AddItemCommand(shopping_cart, "Monitor"))
    cart_history_manager.undo_last_command()
    print(f"[Main] Shopping cart items: {shopping_cart.items}")
    print("[Main] Program ended")

if __name__ == "__main__":
    main()