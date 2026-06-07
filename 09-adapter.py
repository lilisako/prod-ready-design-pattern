
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

def main():
    print("[Main] Starting the program")
    stripe_external_api = StripeExternalAPI()
    stripe_external_adapter = StripeExternalAdapter(stripe_external_api)
    stripe_external_adapter.pay(100)
    print("[Main] Program ended")

if __name__ == "__main__":
    main()