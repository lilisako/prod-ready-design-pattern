# Applying Layered Architecture
We've seen many design patterns so far. These design patterns are a way to solve common problems in software development. However, when you are building a large-scale system, you need to consider the architecture of your system. Layered Architecture is a way to structure your system in a way that is easy to understand, maintain, and scale.
In this article, we will focus on applying layered architecture rather than the theoretical aspects.

The main idea of Layered Architecture is to separate the concerns of your system into different layers.
- Infrastructure Layer: external services, database, etc.
- Domain Layer: business logic, entities
- Application Layer: use cases
- Presentation Layer: handles the user interface and the request/response

And the data flow is User -> Presentation Layer -> Application Layer -> Domain Layer -> Infrastructure Layer.

## Bad Example
First, let's see a bad example of a system that doesn't follow the layered architecture principles. OrderService class is responsible for the entire process including:
- Business Logic
  - Validating the request
  - Calculatinig the total price
  - Checking the stock 
  - Applying the coupon code
- Infrastructure Logic
  - Contacting outside services like Stripe, Sendgrid, database, etc.
- Presentation Logic
  - Parsing the JSON request body
  - Returning the response in JSON format

This makes the code hard to understand, maintain, scale and test. For example, if we want to change the structure of cart_items, we need to modify many parts of the OrderService class. If we want to test just one part of the code, we still need to mock the entire system.
```python
class OrderService:
    def __init(self):
        self.db_connection = "FAKE_CONNECTION"
        self.strip_api_key = "FAKE_API_KEY"
        self.sendgrid_api_key = "FAKE_API_KEY"
    
    def checkout_api_endpoint(self, raw_http_body: dict) -> bool:
        print("Processing order...")

        # Presentation Logic
        user_id = raw_http_body.get("user_id")
        cart_items = raw_http_body.get("cart_items", [])
        coupon_code = raw_http_body.get("coupon_code", "")

        if not user_id or not cart_items:
            print("[ERROR] User ID or cart items are missing")
            return {"status_code": 400, "message": "User ID or cart items are missing"}
        
        # Infrastructure Logic
        print("[INFRASTRUCTURE] Connecting to database...")
        print("[INFRASTRUCTURE] Executing SQL query...")

        total_price = 0
        for item in cart_items:
            stock = 10
            # Business Logic(Validating the stock)
            if stock < item["quantity"]:
                print("[ERROR] Insufficient stock for item: ", item["name"])
                return {"status_code": 400, "message": "Insufficient stock for item: " + item["name"]}
            # Business Logic(Calculating the total price)
            total_price += item["price"] * item["quantity"]
        
        # Business Logic(Applying the coupon code)
        if coupon_code == "SUMMER_SALE" and total_price > 100:
            total_price -= 10
            print("[COUPON] Applied 10% discount")
        
        # Infrastructure Logic(Calling Stripe API to charge the user)
        print("[INFRASTRUCTURE] Calling Stripe API to charge the user...")
        print("[INFRASTRUCTURE] Stripe API returned success")

        # Infrastructure Logic(Saving order to database)
        print("[INFRASTRUCTURE] Saving order to database...")
        print("[INFRASTRUCTURE] Order saved successfully")

        # Infrastructure Logic(Sending email to user)
        print("[INFRASTRUCTURE] Sending email to user...")
        print("[INFRASTRUCTURE] Email sent successfully")

        # Presentation Logic(Returning the response in JSON format)
        order_id = "ORD-LEGACY-1111"
        return {
            "status_code": 200, 
            "message": "Order placed successfully", 
            "total_price": total_price, 
            "order_id": order_id
        }

if __name__ == "__main__":
    order_service = OrderService()
    mock_http_body = {
        "user_id": "USER-LEGACY-1111",
        "cart_items": [
            {"name": "Product 1", "price": 100, "quantity": 1},
            {"name": "Product 2", "price": 200, "quantity": 2}
        ],
        "coupon_code": "SUMMER_SALE"
    }
    print(order_service.checkout_api_endpoint(mock_http_body))
```
Let's make some changes to the code to make it more maintainable and testable. We will make sure that one class is responsible for one thing only. Let's review the principles of layered architecture along with the changes we make.

### Domain Layer
The Domain Layer is responsible for the business logic of the system. For this example, we will create an Order entity to encapsulate the business logic.

```python
class Order:
    def __init__(self, user_id: str, cart_items: list, coupon_code: str):
        self.user_id = user_id
        self.cart_items = cart_items
        self.coupon_code = coupon_code
        self.order_id = "ORD-NEW-1111"
    
    def calculate_total_price(self) -> float:
        total_price = 0
        for item in self.cart_items:
            total_price += item["price"] * item["quantity"]

            if self.coupon_code == "SUMMER_SALE" and total_price > 100:
                total_price -= 10
                print("[COUPON] Applied 10% discount")
        return total_price
```
### Application Layer
The Application Layer is responsible for the business use cases of the system. It contains the interactors (which orchestrate the flow of data to and from the entities) as well as the Ports (interfaces) used to communicate with the external world without coupling to it.

```python
from abc import ABC, abstractmethod
class PaymentPort(ABC):
    @abstractmethod
    def charge(self, amount: float) -> bool:
        pass

class NotificationPort(ABC):
    @abstractmethod
    def send_email(self) -> bool:
        pass

class DatabasePort(ABC):
    @abstractmethod
    def save_order(self, order: Order) -> bool:
        pass

class CheckoutInteractor:
    def __init__(self, payment_port: PaymentPort, notification_port: NotificationPort, database_port: DatabasePort):
        self.payment_port = payment_port
        self.notification_port = notification_port
        self.database_port = database_port
    
    def execute(self, user_id: str, cart_items: list, coupon_code: str) -> dict:
        order = Order(user_id, cart_items, coupon_code)
        total_price = order.calculate_total_price()

        if not self.payment_port.charge(total_price):
            return Exception("Payment failed")

        if not self.database_port.save_order(order):
            return Exception("Order not saved")
        
        self.notification_port.send_email()

        return {"order_id": order.order_id, "total_price": total_price, "status_code": 200}
```

### Infrastructure Layer
Next, let's handle the infrastructure logic. The Infrastructure Layer is responsible for the external services like database, API, etc. Here, we implement the actual gateways and create adapters that implement the Ports defined in the Application Layer. This keeps our core application independent of external changes.

```python
class StripeAPIGateway:
    def __init__(self):
        self.api_key = "FAKE_API_KEY"
    
    def charge(self, amount: float) -> bool:
        print("[INFRASTRUCTURE] Calling Stripe API to charge the user...")
        print("[INFRASTRUCTURE] Stripe API returned success")
        return True
    
class SendgridAPIGateway:
    def __init__(self):
        self.api_key = "FAKE_API_KEY"
    def send_email(self) -> bool:
        print("[INFRASTRUCTURE] Sending email to user...")
        print("[INFRASTRUCTURE] Email sent successfully")
        return True

class DatabaseGateway:
    def __init__(self):
        self.connection = "FAKE_CONNECTION"
    def execute_query(self, query: str) -> bool:
        print("[INFRASTRUCTURE] Executing SQL query...")
        print("[INFRASTRUCTURE] SQL query executed successfully")
        return True

class StripePaymentAdapter(PaymentPort):
    def __init__(self, stripe_api_gateway: StripeAPIGateway):
        self.stripe_api_gateway = stripe_api_gateway
    
    def charge(self, amount: float) -> bool:
        return self.stripe_api_gateway.charge(amount)

class NotificationAdapter(NotificationPort):
    def __init__(self, sendgrid_api_gateway: SendgridAPIGateway):
        self.sendgrid_api_gateway = sendgrid_api_gateway
    
    def send_email(self) -> bool:
        return self.sendgrid_api_gateway.send_email()

class DatabaseAdapter(DatabasePort):
    def __init__(self, database_gateway: DatabaseGateway):
        self.database_gateway = database_gateway
    
    def save_order(self, order: Order) -> bool:
        return self.database_gateway.execute_query("SOME QUERY")
```

### Presentation Layer
The presentation layer is responsible for the user interface and the request/response. 

```python
class CheckoutController:
    def __init__(self, checkout_interactor: CheckoutInteractor):
        self.checkout_interactor = checkout_interactor
    
    def handle(self, raw_http_body: dict) -> dict:
        user_id = raw_http_body.get("user_id")
        cart_items = raw_http_body.get("cart_items", [])
        coupon_code = raw_http_body.get("coupon_code", "")
        try:
            result = self.checkout_interactor.execute(user_id, cart_items, coupon_code)
            return {"status_code": 200, "message": result}
        except Exception as e:
            return {"status_code": 500, "message": str(e)}
```

Now, let's put all the pieces together.
```python
from abc import ABC, abstractmethod

class StripeAPIGateway:
    def __init__(self):
        self.api_key = "FAKE_API_KEY"
    
    def charge(self, amount: float) -> bool:
        print("[INFRASTRUCTURE] Calling Stripe API to charge the user...")
        print("[INFRASTRUCTURE] Stripe API returned success")
        return True
    
class SendgridAPIGateway:
    def __init__(self):
        self.api_key = "FAKE_API_KEY"
    def send_email(self) -> bool:
        print("[INFRASTRUCTURE] Sending email to user...")
        print("[INFRASTRUCTURE] Email sent successfully")
        return True

class DatabaseGateway:
    def __init__(self):
        self.connection = "FAKE_CONNECTION"
    def execute_query(self, query: str) -> bool:
        print("[INFRASTRUCTURE] Executing SQL query...")
        print("[INFRASTRUCTURE] SQL query executed successfully")
        return True

class PaymentPort(ABC):
    @abstractmethod
    def charge(self, amount: float) -> bool:
        pass

class NotificationPort(ABC):
    @abstractmethod
    def send_email(self) -> bool:
        pass

class DatabasePort(ABC):
    @abstractmethod
    def save_order(self, order: Order) -> bool:
        pass

class StripePaymentAdapter(PaymentPort):
    def __init__(self, stripe_api_gateway: StripeAPIGateway):
        self.stripe_api_gateway = stripe_api_gateway
    
    def charge(self, amount: float) -> bool:
        return self.stripe_api_gateway.charge(amount)

class NotificationAdapter(NotificationPort):
    def __init__(self, sendgrid_api_gateway: SendgridAPIGateway):
        self.sendgrid_api_gateway = sendgrid_api_gateway
    
    def send_email(self) -> bool:
        return self.sendgrid_api_gateway.send_email()

class DatabaseAdapter(DatabasePort):
    def __init__(self, database_gateway: DatabaseGateway):
        self.database_gateway = database_gateway
    
    def save_order(self, order: Order) -> bool:
        return self.database_gateway.execute_query("SOME QUERY")

class Order:
    def __init__(self, user_id: str, cart_items: list, coupon_code: str):
        self.user_id = user_id
        self.cart_items = cart_items
        self.coupon_code = coupon_code
        self.order_id = "ORD-NEW-1111"
    
    def calculate_total_price(self) -> float:
        total_price = 0
        for item in self.cart_items:
            total_price += item["price"] * item["quantity"]

            if self.coupon_code == "SUMMER_SALE" and total_price > 100:
                total_price -= 10
                print("[COUPON] Applied 10% discount")
        return total_price


class CheckoutInteractor:
    def __init__(self, payment_port: PaymentPort, notification_port: NotificationPort, database_port: DatabasePort):
        self.payment_port = payment_port
        self.notification_port = notification_port
        self.database_port = database_port
    
    def execute(self, user_id: str, cart_items: list, coupon_code: str) -> dict:
        order = Order(user_id, cart_items, coupon_code)
        total_price = order.calculate_total_price()

        if not self.payment_port.charge(total_price):
            return Exception("Payment failed")

        if not self.database_port.save_order(order):
            return Exception("Order not saved")
        
        self.notification_port.send_email()

        return {"order_id": order.order_id, "total_price": total_price, "status_code": 200}

class CheckoutController:
    def __init__(self, checkout_interactor: CheckoutInteractor):
        self.checkout_interactor = checkout_interactor
    
    def handle(self, raw_http_body: dict) -> dict:
        user_id = raw_http_body.get("user_id")
        cart_items = raw_http_body.get("cart_items", [])
        coupon_code = raw_http_body.get("coupon_code", "")
        try:
            result = self.checkout_interactor.execute(user_id, cart_items, coupon_code)
            return {"status_code": 200, "message": result}
        except Exception as e:
            return {"status_code": 500, "message": str(e)}

stripe_api_gateway = StripeAPIGateway()
sendgrid_api_gateway = SendgridAPIGateway()
database_gateway = DatabaseGateway()

payment_adapter = StripePaymentAdapter(stripe_api_gateway)
notification_adapter = NotificationAdapter(sendgrid_api_gateway)
database_adapter = DatabaseAdapter(database_gateway)

checkout_interactor = CheckoutInteractor(payment_adapter, notification_adapter, database_adapter)
checkout_controller = CheckoutController(checkout_interactor)

mock_http_body = {
    "user_id": "USER_ID",
    "cart_items": [
        {"name": "Product 1", "price": 100, "quantity": 1},
        {"name": "Product 2", "price": 200, "quantity": 2}
    ],
    "coupon_code": "SUMMER_SALE"
}
response = checkout_controller.handle(mock_http_body)
print(response)
```
Here is the result of the code:
```
[COUPON] Applied 10% discount
[INFRASTRUCTURE] Calling Stripe API to charge the user...
[INFRASTRUCTURE] Stripe API returned success
[INFRASTRUCTURE] Executing SQL query...
[INFRASTRUCTURE] SQL query executed successfully
[INFRASTRUCTURE] Sending email to user...
[INFRASTRUCTURE] Email sent successfully
{'status_code': 200, 'message': {'order_id': 'ORD-NEW-1111', 'total_price': 490, 'status_code': 200}}
```
