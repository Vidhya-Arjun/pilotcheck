# Class starts
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        print("Addition operation of two numbers: {} + {}".format(self.x, self.y));
        return self.x + self.y

    def subtract(self):
        print("Subtraction operation of two numbers: {} - {}".format(self.x, self.y));
        return self.x - self.y

    def multiply(self):
        print("multiplication operation of two numbers: {} * {}".format(self.x, self.y));
        return self.x * self.y

    def divide(self):
        print("Divide operation of two numbers: {} / {}".format(self.x, self.y));
        try:
            return self.x / self.y
        except ZeroDivisionError:
            return "Divide by Zero not allowed!"
# Class ends

# Implementation
a, b = 10, 5
calc = Calculator(a, b)
print("Class Add:", calc.add())
print("Class Subtract:", calc.subtract())
print("Class Multiply:", calc.multiply())
print("Class Divide:", calc.divide())
print("End of class program")