class Calculator:
    def __init__(self, a: float, b:float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation
    
    def calculate(self):
        if self.operation == '+':
            return self.a + self.b
        elif self.operation == '-':
            return self.a - self.b
        elif self.operation == '*':
            return self.a * self.b
        elif self.operation == '/':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero is not allowed"
        else:
            return "Invalid operation!"

if __name__ == "__main__":
    a = float(input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))
    operation = input("Enter operation (+ , - , * , /): ") 

    calc = Calculator(a,b,operation)
    result = calc.calculate()
    print("Result: ", result)