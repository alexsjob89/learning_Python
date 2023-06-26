def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b

def compare(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is less than {b}"
    else:
        return f"{a} is equal to {b}"
def is_same(a, b):
    if a is b:
        return "a and b point to the same object."
    else:
        return "a and b do not point to the same object."


def main():
    print("Welcome to Basic Python Calculator!")

    a = int(input("Enter a number for 'a': "))
    b = int(input("Enter a number for 'b': "))

    operation = int(input(
        "\nChoose an operation: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Compare if a and b are the same object \n"))

    if operation == 1:
        print(f"The result is: {add(a, b)}")
    elif operation == 2:
        print(f"The result is: {subtract(a, b)}")
    elif operation == 3:
        print(f"The result is: {multiply(a, b)}")
    elif operation == 4:
        print(f"The result is : {divide(a, b)}")
    elif operation == 5:
        print(f"The result is: {compare(a, b)}")
    elif operation == 6:
        print(f"The result is: {is_same(a, b)}")
    else:
        print("Invalid operation selected.")


if __name__ == "__main__":
    main()