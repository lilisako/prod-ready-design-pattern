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

def main():
    print("[Main] Starting the program")
    logger1 = DatabaseLogger()
    logger1.log("Payment successful for $100")

    logger2 = DatabaseLogger()
    logger2.log("Payment failed for $200")

    print(f"[Main] logger1 and logger2 are the same instance: {logger1 is logger2}")
    print(f"[Main] logger1 logs: {logger1.logs}")
    print(f"[Main] logger2 logs: {logger2.logs}")

    print("[Main] Program ended")

if __name__ == "__main__":
    main()