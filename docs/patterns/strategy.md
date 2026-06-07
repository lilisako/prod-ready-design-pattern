# Strategy Pattern

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
