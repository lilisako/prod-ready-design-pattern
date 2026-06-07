class OrderComponent:
    def get_total_price(self) -> float:
        pass 
    
    def get_description(self) -> str:
        pass

class BaseOrder(OrderComponent):
    def get_total_price(self) -> float:
        return 100
    
    def get_description(self) -> str:
        return "Base Order"

class ExpressShippingDecorator(OrderComponent):
    def __init__(self, order: OrderComponent):
        self.order = order
    
    def get_total_price(self) -> float:
        return self.order.get_total_price() + 10
    
    def get_description(self) -> str:
        return self.order.get_description() + ", Express Shipping"

class GiftWrapDecorator(OrderComponent):
    def __init__(self, order: OrderComponent):
        self.order = order
    
    def get_total_price(self) -> float:
        return self.order.get_total_price() + 5
    
    def get_description(self) -> str:
        return self.order.get_description() + ", Gift Wrap"

def main():
    print("[Main] Starting the program")
    base_order = BaseOrder()
    print(f"[Main] Base order: {base_order.get_description()}, Total price: ${base_order.get_total_price()}")
    express_shipping = ExpressShippingDecorator(base_order)
    print(f"[Main] Express shipping: {express_shipping.get_description()}, Total price: ${express_shipping.get_total_price()}")
    gift_wrap = GiftWrapDecorator(express_shipping)
    print(f"[Main] Gift wrap: {gift_wrap.get_description()}, Total price: ${gift_wrap.get_total_price()}")
    print("[Main] Program ended")

if __name__ == "__main__":
    main()
