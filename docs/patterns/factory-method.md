# Factory Method Pattern

Factory Method Pattern is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. 

For example, you have a order system for your e-commerce website and you want to create a different order for physical and digital products. For both of the orders, you need a different process to fulfill the order. With Factory method pattern, you can easily create a different order without changing the existing code. When you call the fulfill_order() method, you don't need to know the details of the order. You just need to call the fulfill_order() method and the order will be created and processed.

```python
class Order:
    def __init__(self, amount: float):
        self.amount = amount
    
    def process(self) -> None:
        pass

class PhysicalOrder(Order):
    def process(self) -> None:
        print(f"[PhysicalOrder] Processing order of ${self.amount}")

class DigitalOrder(Order):
    def process(self) -> None:
        print(f"[DigitalOrder] Processing order of ${self.amount}")

class OrderFactory:
    def create_order(self, amount: float) -> Order:
        pass
    
    def fulfill_order(self, amount: float) -> None:
        order = self.create_order(amount)
        order.process()

class PhysicalOrderFactory(OrderFactory):
    def create_order(self, amount: float) -> Order:
        return PhysicalOrder(amount)

class DigitalOrderFactory(OrderFactory):
    def create_order(self, amount: float) -> Order:
        return DigitalOrder(amount)

print("[Main] Starting the program")
order_factory = PhysicalOrderFactory()
order_factory.fulfill_order(100)
order_factory = DigitalOrderFactory()
order_factory.fulfill_order(100)
print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[PhysicalOrder] Processing order of $100
[DigitalOrder] Processing order of $100
[Main] Program ended
```
