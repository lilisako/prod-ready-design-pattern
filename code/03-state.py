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


def main():
    print("[Main] Starting the program")
    order = Order()

    print("\n--- 1. Current State: Pending Payment ---")
    order.ship()

    print("\n--- 2. Current State: Shipped ---")
    order.set_state(ShippedState())
    order.ship() 
    order.cancel()

    print("\n[Main] Program ended")

if __name__ == "__main__":
    main()