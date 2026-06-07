# Chain of Responsibility Pattern

Chain of Responsibility Pattern is a behavioral design pattern that allows you to pass requests along a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain. This pattern is useful when you have a chain of handlers and you want to process the request by the first handler that can handle it.

For example, before checkout, you want to check if the order is fraudulent, if the stock is available, if the coupon is valid, etc. With Chain of Responsibility pattern, you can easily add a new handler without changing the existing code. Here is an example of Chain of Responsibility pattern in Python:

```python
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

print("[Main] Starting the program")
fraud_checker = FraudCheckerHandler()
stock_check = StockCheckHandler()
coupon_checker = CouponCheckerHandler()
fraud_checker.set_next_handler(stock_check)
stock_check.set_next_handler(coupon_checker)
fraud_checker.handle(Order(amount=100, stock=10, coupon_code="VALID"))
fraud_checker.handle(Order(amount=100_000, stock=10, coupon_code="VALID"))
print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[FraudCheckerHandler] Checking for fraud...
[StockCheckHandler] Checking for stock...
[CouponCheckerHandler] Checking for coupon...
[FraudCheckerHandler] Checking for fraud...
[FraudCheckerHandler] Amount is too high, order cancelled
[Main] Program ended
```
