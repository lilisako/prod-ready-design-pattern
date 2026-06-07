class PaymentImplementor:
    def execute_payment(self, amount: float) -> None:
        pass

class CreditCardPayment(PaymentImplementor):
    def execute_payment(self, amount: float) -> None:
        print(f"[CreditCardPayment] Executing payment of ${amount}...")

class BankTransferPayment(PaymentImplementor):
    def execute_payment(self, amount: float) -> None:
        print(f"[BankTransferPayment] Executing payment of ${amount}...")

class Order:
    def __init__(self, amount: float, payment_implementor: PaymentImplementor):
        self.amount = amount
        self.payment_implementor = payment_implementor
    
    def process(self) -> None:
        pass

class StandardOrder(Order):
    def process(self) -> None:
        print(f"[StandardOrder] Processing order...")
        self.payment_implementor.execute_payment(self.amount)
        

class ExpressOrder(Order):
    def process(self) -> None:
        print(f"[ExpressOrder] Processing order...")
        self.payment_implementor.execute_payment(self.amount + 10)

def main():
    print("[Main] Starting the program")
    credit_card_payment = CreditCardPayment()
    bank_transfer_payment = BankTransferPayment()
    standard_order = StandardOrder(100, credit_card_payment)
    standard_order.process()
    express_order = ExpressOrder(100, bank_transfer_payment)
    express_order.process()
    print("[Main] Program ended")

if __name__ == "__main__":
    main()