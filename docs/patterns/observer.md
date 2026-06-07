# Observer Pattern

Observer Pattern is a behavioral design pattern that allows you to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. This pattern is useful when you have multiple objects that need to be notified when another object changes state.
For example, you have a payment system for your e-commerce website and you want to notify the stock manager and the analytics when a payment is successful. With Observer pattern, you can easily add a new listener without changing the existing code. Here is an example of Observer pattern in Python:

```python
class PaymentProcessor:
    def __init__(self):
        self.listeners = []
    
    def add_listener(self, listener: Listener):
        self.listeners.append(listener)
    
    def remove_listener(self, listener: Listener):
        self.listeners.remove(listener)
    
    def notify_listeners(self, amount: float):
        for listener in self.listeners:
            listener.on_payment(amount)

class Listener:
    def on_payment(self, amount: float):
        pass

class PaymentListener(Listener):
    def on_payment(self, amount: float):
        print(f"[Listener] Sending email notification for payment of ${amount}..")

class StockManageListener(Listener):
    def on_payment(self, amount: float):
        print(f"[Listener] Updating stock for payment of ${amount}..")

class AnalyticsListener(Listener):
    def on_payment(self, amount: float):
        print(f"[Listener] Updating analytics..")

print("[Main] Starting the program")
payment_processor = PaymentProcessor()
payment_listener = PaymentListener()
stock_manager_listener = StockManageListener()
analytics_listener = AnalyticsListener()
payment_processor.add_listener(payment_listener)
payment_processor.add_listener(stock_manager_listener)
payment_processor.add_listener(analytics_listener)

print("[Main] Successfully User A finished payment of $100")
payment_processor.notify_listeners(100)

# The specification changed and now there is no need to update the analytics
print("[Main] Successfully User B finished payment of $200")
payment_processor.remove_listener(analytics_listener)
payment_processor.notify_listeners(200)

print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[Main] Successfully User A finished payment of $100
[Listener] Sending email notification for payment of $100..
[Listener] Updating stock for payment of $100..
[Listener] Updating analytics..
[Main] Successfully User B finished payment of $200
[Listener] Sending email notification for payment of $200..
[Listener] Updating stock for payment of $200..
[Main] Program ended
```
