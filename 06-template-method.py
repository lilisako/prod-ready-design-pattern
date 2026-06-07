class AbstractShippingProcess:
    def calculate_fee(self, weight: float) -> float:
        pass
    
    def generate_label(self) -> str:
        pass
    
    def ship_order(self, weight: float) -> None:
        print(f"[Shipping] Shipping {weight}kg order...")
        print(f"[Shipping] Fee: ${self.calculate_fee(weight)}")
        print(f"[Shipping] Label: {self.generate_label()}")

class DomesticShippingProcess(AbstractShippingProcess):
    def calculate_fee(self, weight: float) -> float:
        return weight * 1.5
    
    def generate_label(self) -> str:
        return "Domestic Shipping Label"

class InternationalShippingProcess(AbstractShippingProcess):
    def calculate_fee(self, weight: float) -> float:
        return weight * 2.5

    def generate_label(self) -> str:
        return "International Shipping Label"

def main():
    print("[Main] Starting the program")
    domestic_shipping = DomesticShippingProcess()
    international_shipping = InternationalShippingProcess()
    domestic_shipping.ship_order(100)
    international_shipping.ship_order(100)
    print("[Main] Program ended")

if __name__ == "__main__":
    main()
