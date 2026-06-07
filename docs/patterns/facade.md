# Facade Pattern

Facade Pattern is a structural design pattern that provides a simplified interface to a complex subsystem. This pattern is useful when you have a complex system with multiple subsystems and you want to simplify the interface for the client. For example, you have a payment system for your e-commerce website and after the payment is successful, you want to execute multiple actions like updating the order status to shipped and sending a notification to the customer. With Facade pattern, you can easily execute these actions without knowing the details of the subsystems. Here is an example of Facade pattern in Python:

You don't need to know the details of what happens inside the subsystems. You just need to know the interface of the facade.

```python
class PaymentSystem:
    def process_payment(self, amount: float) -> None:
        print(f"[PaymentSystem] Processing payment of ${amount}...")

class OrderSystem:
    def update_to_shipped(self) -> None:
        print(f"[OrderSystem] Updating order to shipped...")

class NotificationSystem:
    def send_notification(self, message: str) -> None:
        print(f"[NotificationSystem] Sending notification: {message}...")

class Facade:
    def __init__(self):
        self.payment_system = PaymentSystem()
        self.order_system = OrderSystem()
        self.notification_system = NotificationSystem()

    def process_order(self, amount: float) -> None:
        self.payment_system.process_payment(amount)
        self.order_system.update_to_shipped()
        self.notification_system.send_notification("Order shipped successfully")

print("[Main] Starting the program")
facade = Facade()
facade.process_order(100)
print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[PaymentSystem] Processing payment of $100...
[OrderSystem] Updating order to shipped...
[NotificationSystem] Sending notification: Order shipped successfully...
[Main] Program ended
```
