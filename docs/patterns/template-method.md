# Template Method Pattern

Template Method Pattern is a behavioral design pattern that defines the skeleton of an algorithm in a method, deferring some steps to subclasses. This pattern is useful when you have a algorithm with multiple steps and you want to allow subclasses to override some of the steps. 

For example, you have a shipping system for your e-commerce website and you want to build a different shipping process for domestic and international orders. For both of the processes, you need to calculate the fee and generate a label. With Template method pattern, you can easily define the skeleton of the algorithm and let the subclasses to implement the specific steps. 

What we are doing here is just inheriting the abstract class and implementing the specific steps. However by defining the skeleton of the algorithm in the abstract class(ship_order() method), we can ensure that the specific steps are executed in the correct order.

Here is an example of Template method pattern in Python:

```python
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

print("[Main] Starting the program")
domestic_shipping = DomesticShippingProcess()
international_shipping = InternationalShippingProcess()
domestic_shipping.ship_order(100)
international_shipping.ship_order(100)
print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[Shipping] Shipping 100kg order...
[Shipping] Fee: $150.0
[Shipping] Label: Domestic Shipping Label
[Shipping] Shipping 100kg order...
[Shipping] Fee: $250.0
[Shipping] Label: International Shipping Label
[Main] Program ended
```

## Problem with Template method pattern
Template method pattern is quite simple but it's not very flexible. Especially when you want to add a new method to the interface, you need to make sure that all the subclasses behave correctly. 

For example, you have different types of users in your system: premium, guest, basic, etc. And you want to add a new user action to only premium users, but not other users. Here is an example in Go:

As you can see that Guest User and Basic User don't have the new user action and but still need to implement those methods. This will lead to code duplication and it becomes harder to read and understand the code.

```go
type UserAction interface {
    LogIn()
    SaveToDatabase()
    GiveBonusPoints()
    GenerateMonthlyReport()
}

type PremiumUser struct {}
func (u *PremiumUser) LogIn() {
    fmt.Println("Premium user logged in")
}
func (u *PremiumUser) SaveToDatabase() {
    fmt.Println("Premium user saved to database")
}
func (u *PremiumUser) GiveBonusPoints() {
    fmt.Println("Premium user gives 100 bonus points")
}
func (u *PremiumUser) GenerateMonthlyReport() {
    fmt.Println("Premium user generates monthly report")
}

func GuestUser struct {}
func (u *GuestUser) LogIn() {
    fmt.Println("Guest user logged in")
}
func (u *GuestUser) SaveToDatabase() {
    // Do nothing
}
func (u *GuestUser) GiveBonusPoints() {
    // Do nothing
}
func (u *GuestUser) GenerateMonthlyReport() {
    // Do nothing
}

func BasicUser struct {}
func (u *BasicUser) LogIn() {
    fmt.Println("Basic user logged in")
}
func (u *BasicUser) SaveToDatabase() {
    fmt.Println("Basic user saved to database")
}
func (u *BasicUser) GiveBonusPoints() {
    // Do nothing
}
func (u *BasicUser) GenerateMonthlyReport() {
    // Do nothing
}

func main() {
    for _, user := range users {
        user.LogIn()
        user.SaveToDatabase()
        user.GiveBonusPoints()
        user.GenerateMonthlyReport()
    }
}
```
