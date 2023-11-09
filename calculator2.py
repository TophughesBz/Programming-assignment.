//Maina Chrispin Nguru
//SCT211-0006/2022

class Calculator:
    def calculate(self, num1,operator,num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Cannot divide by zero"
            return num1 / num2
        else:
            return "Invalid operator"

num1=int(input("Enter your first number :"))
operator=(input("Enter your operator :"))
num2=int(input("Enter your second number :"))

print(f"{num1} {operator} {num2} =",Calculator.calculate(Calculator,num1,operator,num2))
