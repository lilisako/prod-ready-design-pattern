class Order:
    def __init__(self, amount: float, stock: int, coupon_code: str):
        self.amount = amount
        self.stock = stock
        self.coupon_code = coupon_code

class OrderHandler:
    def __init__(self, next_handler: 'OrderHandler' = None):
        self.next_handler = next_handler
    
    def set_next_handler(self, next_handler: 'OrderHandler'):
        self.next_handler = next_handler

    def handle(self, order: Order) -> None:
        pass

class FraudCheckerHandler(OrderHandler):
    def handle(self, order: Order) -> None:
        print("[FraudCheckerHandler] Checking for fraud...")
        if order.amount > 1000:
            print("[FraudCheckerHandler] Amount is too high, order cancelled")
            return
        if self.next_handler:
            self.next_handler.handle(order)

class StockCheckHandler(OrderHandler):
    def handle(self, order: Order) -> None:
        print("[StockCheckHandler] Checking for stock...")
        if order.stock == 0:
            print("[StockCheckHandler] Stock is out, order cancelled")
            return
        if self.next_handler:
            self.next_handler.handle(order)

class CouponCheckerHandler(OrderHandler):
    def handle(self, order: Order) -> None:
        print("[CouponCheckerHandler] Checking for coupon...")
        if order.coupon_code == "EXPIRED":
            print("[CouponCheckerHandler] Coupon is invalid, order cancelled")
            return
        if self.next_handler:
            self.next_handler.handle(order)

def main():
    print("[Main] Starting the program")
    fraud_checker = FraudCheckerHandler()
    stock_check = StockCheckHandler()
    coupon_checker = CouponCheckerHandler()
    fraud_checker.set_next_handler(stock_check)
    stock_check.set_next_handler(coupon_checker)
    fraud_checker.handle(Order(amount=100, stock=10, coupon_code="VALID"))
    fraud_checker.handle(Order(amount=100_000, stock=10, coupon_code="VALID"))
    print("[Main] Program ended")

if __name__ == "__main__":
    main()