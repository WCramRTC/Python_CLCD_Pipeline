class SimpleCalculator:

    def add(self, number1, number2):
        return number1 + number2
    
    def subtract(self, number1, number2):
        return number1 - number2
    
# Test Calculator

calculator = SimpleCalculator()

value = calculator.add(1,2)

print(value)