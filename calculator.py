def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


if __name__ == "__main__":
    print("Add:", add(2, 3))
    print("Subtract:", subtract(5, 2))
    print("Multiply:", multiply(2, 3))
    print("Divide:", divide(6, 2))