# Template Method Pattern

Template Method Pattern is a behavioral design pattern that defines the skeleton of an algorithm in a method, deferring some steps to subclasses. This pattern is useful when you have a algorithm with multiple steps and you want to allow subclasses to override some of the steps. 

For example, you have a shipping system for your e-commerce website and you want to build a different shipping process for domestic and international orders. For both of the processes, you need to calculate the fee and generate a label. With Template method pattern, you can easily define the skeleton of the algorithm and let the subclasses to implement the specific steps. 

What we are doing here is just inheriting the abstract class and implementing the specific steps. However by defining the skeleton of the algorithm in the abstract class(ship_order() method), we can ensure that the specific steps are executed in the correct order.

Here is an example of Template method pattern in Python:

```python
class AbstractShippingProcess:
    def calculate_fee(self, weight: float) -> float:
        pass
    
    def generate_label(self) -> str:
        pass
    
    def ship_order(self, weight: float) -> None:
        print(f"[Shipping] Shipping {weight}kg order...")
        print(f"[Shipping] Fee: ${self.calculate_fee(weight)}")
        print(f"[Shipping] Label: {self.generate_label()}")

class DomesticShippingProcess(AbstractShippingProcess):
    def calculate_fee(self, weight: float) -> float:
        return weight * 1.5
    
    def generate_label(self) -> str:
        return "Domestic Shipping Label"

class InternationalShippingProcess(AbstractShippingProcess):
    def calculate_fee(self, weight: float) -> float:
        return weight * 2.5

    def generate_label(self) -> str:
        return "International Shipping Label"

print("[Main] Starting the program")
domestic_shipping = DomesticShippingProcess()
international_shipping = InternationalShippingProcess()
domestic_shipping.ship_order(100)
international_shipping.ship_order(100)
print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[Shipping] Shipping 100kg order...
[Shipping] Fee: $150.0
[Shipping] Label: Domestic Shipping Label
[Shipping] Shipping 100kg order...
[Shipping] Fee: $250.0
[Shipping] Label: International Shipping Label
[Main] Program ended
```
