# Adapter Pattern

Adapter pattern is a structural design pattern that allows you to adapt an interface to another interface. For example, you have a payment system for your e-commerce website and you want to use a third-party payment gateway like Stripe. With Adapter pattern, you can easily adapt the Stripe API to the payment system interface. Let's say the third party payment gateway has a different interface(make_charge() method) than the payment system interface(pay() method).

Here is an example of Adapter pattern in Python:

```python

class PaymentStrategy:
    def pay(self, amount: float) -> None:
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"[Strategy] Paying {amount} with credit card")

class StripeExternalAPI:
    def make_charge(self, amount: float) -> None:
        print(f"[API] Making charge of {amount} with Stripe")

class StripeExternalAdapter(PaymentStrategy):
    def __init__(self, stripe_external_api: StripeExternalAPI):
        self.stripe_external_api = stripe_external_api

    def pay(self, amount: float) -> None:
        self.stripe_external_api.make_charge(amount)
        print(f"[Adapter] Paying {amount} with Stripe")

print("[Main] Starting the program")
stripe_external_api = StripeExternalAPI()
stripe_external_adapter = StripeExternalAdapter(stripe_external_api)
stripe_external_adapter.pay(100)
print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[API] Making charge of 100 with Stripe
[Adapter] Paying 100 with Stripe
[Main] Program ended
```
