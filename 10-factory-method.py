class Order:
    def __init__(self, amount: float):
        self.amount = amount
    
    def process(self) -> None:
        pass

class PhysicalOrder(Order):
    def process(self) -> None:
        print(f"[PhysicalOrder] Processing order of ${self.amount}")

class DigitalOrder(Order):
    def process(self) -> None:
        print(f"[DigitalOrder] Processing order of ${self.amount}")

class OrderFactory:
    def create_order(self, amount: float) -> Order:
        pass
    
    def fulfill_order(self, amount: float) -> None:
        order = self.create_order(amount)
        order.process()

class PhysicalOrderFactory(OrderFactory):
    def create_order(self, amount: float) -> Order:
        return PhysicalOrder(amount)

class DigitalOrderFactory(OrderFactory):
    def create_order(self, amount: float) -> Order:
        return DigitalOrder(amount)

def main():
    print("[Main] Starting the program")
    order_factory = PhysicalOrderFactory()
    order_factory.fulfill_order(100)
    order_factory = DigitalOrderFactory()
    order_factory.fulfill_order(100)
    print("[Main] Program ended")

if __name__ == "__main__":
    main()
