# Production-Ready Design Patterns in Python
This repository contains production-ready design patterns in Python. Design Patterns are a way to solve common problems in software development. As you develop your own software, there are many unexpected problems or new requirements that you may not have considered in first place. Design Patters are a way to solve these problems by providing a general solution to these problems.
But you need to be careful when using design patterns. They are handy but they can also make your code more complex. You need to use them wisely and only when they are truly necessary.
In this repository, we will cover some famous design patterns in Python with an example E-Commerce system.


## Strategy Pattern
Strategy Pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each algorithm, and make them interchangeable. This pattern is useful when you have multiple algorithms for a same problem.
For example, you have a payment system for your e-commerce website and you have multiple payment methods like credit card, bank transfer, etc. With Strategy pattern, you can easily add a new payment method without changing the existing code.

Here is an example of Strategy pattern in Python:

```python

class PaymentStrategy:
    def pay(self, amount: float) -> None:
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"[Strategy] Paying {amount} with credit card")


class BankTransferPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"[Strategy] Paying {amount} with bank transfer")

class Order:
    def __init__(self, amount: float):
        self.amount = amount
        self.payment_strategy = None
    
    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def pay(self) -> None:
        if self.payment_strategy is None:
            raise ValueError("[Order] Error: Payment strategy is not set")
        print(f"[Order] Paying {self.amount} with {self.payment_strategy.__class__.__name__}")
        self.payment_strategy.pay(self.amount)

print("[Main] Starting the program")
order = Order(100)
order.set_payment_strategy(CreditCardPayment())
order.pay()
order.set_payment_strategy(BankTransferPayment())
order.pay()
print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[Order] Paying 100 with CreditCardPayment
[Strategy] Paying 100 with credit card
[Order] Paying 100 with BankTransferPayment
[Strategy] Paying 100 with bank transfer
[Main] Program ended
```

## Observer Pattern
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

## State Pattern
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

## Facade Pattern
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

## Decorator Pattern
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

## Template Method Pattern
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

## Chain of Responsibility Pattern
Chain of Responsibility Pattern is a behavioral design pattern that allows you to pass requests along a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain. This pattern is useful when you have a chain of handlers and you want to process the request by the first handler that can handle it.

For example, before checkout, you want to check if the order is fraudulent, if the stock is available, if the coupon is valid, etc. With Chain of Responsibility pattern, you can easily add a new handler without changing the existing code. Here is an example of Chain of Responsibility pattern in Python:

```python
class Order:
    def __init__(self, amount: float, stock: int, coupon_code: str):
        self.amount = amount
        self.stock = stock
        self.coupon_code = coupon_code

class OrderHandler:
    def __init__(self, next_handler: 'OrderHandler' = None):
        self.next_handler = next_handler
    
    def set_next_handler(self, next_handler: 'OrderHandler'):
        self.next_handler = next_handler

    def handle(self, order: Order) -> None:
        pass

class FraudCheckerHandler(OrderHandler):
    def handle(self, order: Order) -> None:
        print("[FraudCheckerHandler] Checking for fraud...")
        if order.amount > 1000:
            print("[FraudCheckerHandler] Amount is too high, order cancelled")
            return
        if self.next_handler:
            self.next_handler.handle(order)

class StockCheckHandler(OrderHandler):
    def handle(self, order: Order) -> None:
        print("[StockCheckHandler] Checking for stock...")
        if order.stock == 0:
            print("[StockCheckHandler] Stock is out, order cancelled")
            return
        if self.next_handler:
            self.next_handler.handle(order)

class CouponCheckerHandler(OrderHandler):
    def handle(self, order: Order) -> None:
        print("[CouponCheckerHandler] Checking for coupon...")
        if order.coupon_code == "EXPIRED":
            print("[CouponCheckerHandler] Coupon is invalid, order cancelled")
            return
        if self.next_handler:
            self.next_handler.handle(order)

print("[Main] Starting the program")
fraud_checker = FraudCheckerHandler()
stock_check = StockCheckHandler()
coupon_checker = CouponCheckerHandler()
fraud_checker.set_next_handler(stock_check)
stock_check.set_next_handler(coupon_checker)
fraud_checker.handle(Order(amount=100, stock=10, coupon_code="VALID"))
fraud_checker.handle(Order(amount=100_000, stock=10, coupon_code="VALID"))
print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[FraudCheckerHandler] Checking for fraud...
[StockCheckHandler] Checking for stock...
[CouponCheckerHandler] Checking for coupon...
[FraudCheckerHandler] Checking for fraud...
[FraudCheckerHandler] Amount is too high, order cancelled
[Main] Program ended
```
