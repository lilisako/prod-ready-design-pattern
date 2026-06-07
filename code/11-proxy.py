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
