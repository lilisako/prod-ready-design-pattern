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

def main():
    print("[Main] Starting the program")
    facade = Facade()
    facade.process_order(100)
    print("[Main] Program ended")

if __name__ == "__main__":
    main()
