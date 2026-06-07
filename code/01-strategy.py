
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

def main():
    print("[Main] Starting the program")
    order = Order(100)
    order.set_payment_strategy(CreditCardPayment())
    order.pay()
    order.set_payment_strategy(BankTransferPayment())
    order.pay()
    print("[Main] Program ended")

if __name__ == "__main__":
    main()