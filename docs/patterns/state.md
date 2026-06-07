# State Pattern

State Pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes. This pattern is useful when you have a state machine with multiple states and you want to change the behavior of the object when it changes its state. For example, you have an order system for your e-commerce website and you want to change the behavior of the order when it is in different states like pending payment, paid, shipped, cancelled. With State pattern, you can easily add a new state without changing the existing code. Here is an example of State pattern in Python:

When the order is in pending payment state, you cannot ship the order until the payment is successful. When the order is in shipped state, you cannot cancel the order. When the order is in cancelled state, you cannot ship the order again. Even if you have a new state like refunded, you cannot ship the order again.

```python
class OrderState:
    def ship_order(self) -> None:
        pass

    def cancel_order(self) -> None:
        pass


class PendingPaymentState(OrderState):
    def ship_order(self):
        print("[Print] [Error] Cannot ship unpaid order. Payment is required.")
    
    def cancel_order(self):
        print("[Print] Order cancelled successfully (No refund required).")


class PaidState(OrderState):
    def ship_order(self):
        print("[Print] Order shipped successfully from the warehouse.")
    
    def cancel_order(self):
        print("[Print] Order cancelled successfully. Initiating refund process.")


class ShippedState(OrderState):
    def ship_order(self):
        print("[Print] [Error] This order has already been shipped.")
    
    def cancel_order(self):
        print("[Print] [Error] Cannot cancel order because it has already been shipped.")


class Order:
    def __init__(self):
        # Default initial state is PendingPayment
        self.state = PendingPaymentState() 
    
    def set_state(self, state: OrderState):
        self.state = state
    
    def ship(self):
        print("[System] Triggering ship action...")
        self.state.ship_order()
    
    def cancel(self):
        print("[System] Triggering cancel action...")
        self.state.cancel_order()

print("[Main] Starting the program")
order = Order()

print("\n--- 1. Current State: Pending Payment ---")
order.ship()

print("\n--- 2. Current State: Shipped ---")
order.set_state(ShippedState())
order.ship() 
order.cancel()

print("\n[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program

--- 1. Current State: Pending Payment ---
[System] Triggering ship action...
[Print] [Error] Cannot ship unpaid order. Payment is required.

--- 2. Current State: Shipped ---
[System] Triggering ship action...
[Print] [Error] This order has already been shipped.
[System] Triggering cancel action...
[Print] [Error] Cannot cancel order because it has already been shipped.

[Main] Program ended
```
