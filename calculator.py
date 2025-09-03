# Class starts
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y
# Class ends

# Implementation
a, b = 10, 5
calc = Calculator(a, b)
print("Class Add:", calc.add())
print("Class Subtract:", calc.subtract())
print("Class Multiply:", calc.multiply())
print("Class Divide:", calc.divide())
print("End of class program")