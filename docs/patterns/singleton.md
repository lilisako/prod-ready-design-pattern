# Singleton Pattern

Singleton Pattern is a creational design pattern that ensures that a class has only one instance and provides a global point of access to it. This pattern is useful when you want to ensure that a class has only one instance and you want to access it globally. 

For example, you have a database logger for your e-commerce website and you want to ensure that there is only one instance of the database logger. Otherwise you will have multiple instances of the database logger and it's quite not efficient memory wise. With Singleton pattern, you can easily ensure that there is only one instance of the database logger. Here is an example of Singleton pattern in Python:

```python
class DatabaseLogger:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseLogger, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if DatabaseLogger._initialized:
            return
        self.logs = []
        DatabaseLogger._initialized = True
    
    def log(self, message: str):
        self.logs.append(message)
        print(f"[DatabaseLogger] [Log] {message}")

print("[Main] Starting the program")
logger1 = DatabaseLogger()
logger1.log("Payment successful for $100")

logger2 = DatabaseLogger()
logger2.log("Payment failed for $200")

print(f"[Main] logger1 and logger2 are the same instance: {logger1 is logger2}")
print(f"[Main] logger1 logs: {logger1.logs}")
print(f"[Main] logger2 logs: {logger2.logs}")

print("[Main] Program ended")
```

Here is the output of the program:

```
[Main] Starting the program
[DatabaseLogger] [Log] Payment successful for $100
[DatabaseLogger] [Log] Payment failed for $200
[Main] logger1 and logger2 are the same instance: True
[Main] logger1 logs: ['Payment successful for $100', 'Payment failed for $200']
[Main] logger2 logs: ['Payment successful for $100', 'Payment failed for $200']
[Main] Program ended
```
