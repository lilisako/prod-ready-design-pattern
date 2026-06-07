# Proxy Pattern

Proxy Pattern is a structural design pattern that provides a surrogate or placeholder for another object to control access to it. This pattern is useful when you want to add a layer of security to an object or to control the access to an object.

For example, you have a payment system for your e-commerce website and you want to add a layer of security to the payment system like logging, validation, etc and you want to control the access to the payment system. Here is an example of Proxy pattern in Python:

```python
class Payment:
    def pay(self, amount: float) -> None:
        pass


class RealPayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"[RealPayment] [Log] Successfully paid ${amount} with credit card.")

class PaymentProxy(Payment):
    def __init__(self):
        self.real_payment = RealPayment()
    
    def pay(self, amount: float) -> None:
        print(f"[Proxy] [Log] Payment request received for ${amount}.")
        if amount > 100:
            print(f"[Proxy] [Log] Payment failed: Amount is too high for ${amount}.")
            return
        self.real_payment.pay(amount)

def main():
    print("[Main] Starting the program")
    payment_proxy = PaymentProxy()
    payment_proxy.pay(100)
    payment_proxy.pay(200)
    print("[Main] Program ended")

if __name__ == "__main__":
    main()
```

Here is the output of the program:

```
[Main] Starting the program
[Proxy] [Log] Payment request received for $100.
[RealPayment] [Log] Successfully paid $100 with credit card.
[Proxy] [Log] Payment request received for $200.
[Proxy] [Log] Payment failed: Amount is too high for $200.
[Main] Program ended
```
