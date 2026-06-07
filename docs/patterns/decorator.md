# Decorator Pattern

Decorator Pattern is a structural design pattern that allows you to dynamically add new behaviors to objects by placing them inside special wrapper objects that contain the behaviors. This pattern is useful when you want to add new functionality to an object without changing its structure. 

For example, when you checkout on your e-commerce website, you can choose a different options like express shipping, gift wrap etc. Depends on the options you choose, the total price of the order will be different. With Decorator pattern, you can easily add a new option without changing the existing code. Here is an example of Decorator pattern in Python:

```python
class OrderComponent:
    def get_total_price(self) -> float:
        pass 
    
    def get_description(self) -> str:
        pass

class BaseOrder(OrderComponent):
    def get_total_price(self) -> float:
        return 100
    
    def get_description(self) -> str:
        return "Base Order"

class ExpressShippingDecorator(OrderComponent):
    def __init__(self, order: OrderComponent):
        self.order = order
    
    def get_total_price(self) -> float:
        return self.order.get_total_price() + 10
    
    def get_description(self) -> str:
        return self.order.get_description() + ", Express Shipping"

class GiftWrapDecorator(OrderComponent):
    def __init__(self, order: OrderComponent):
        self.order = order
    
    def get_total_price(self) -> float:
        return self.order.get_total_price() + 5
    
    def get_description(self) -> str:
        return self.order.get_description() + ", Gift Wrap"

print("[Main] Starting the program")
base_order = BaseOrder()
print(f"[Main] Base order: {base_order.get_description()}, Total price: ${base_order.get_total_price()}")
express_shipping = ExpressShippingDecorator(base_order)
print(f"[Main] Express shipping: {express_shipping.get_description()}, Total price: ${express_shipping.get_total_price()}")
gift_wrap = GiftWrapDecorator(express_shipping)
print(f"[Main] Gift wrap: {gift_wrap.get_description()}, Total price: ${gift_wrap.get_total_price()}")
print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[Main] Base order: Base Order, Total price: $100
[Main] Express shipping: Base Order, Express Shipping, Total price: $110
[Main] Gift wrap: Base Order, Express Shipping, Gift Wrap, Total price: $115
[Main] Program ended
```
