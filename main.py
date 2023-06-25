
def calculator(a, b):
    print(f"\nPerforming calculator on{a} and {b}")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} is greater than {b} is {a > b}")
    print(f"{a} is equal to {b} is {a == b}")
    print(f"{a} and {b} are the same object is {a is b}")

def main():
    print("This is a basic app to demonstrate the use of basic operators in Python.")

    a = int(input("\nEnter a number for 'a': "))
    b = int(input("Enter a number for 'b' : "))

    calculator(a, b)

    my_list = [a, b]
    print(f"\nCreated list: {my_list}")

    check_num = int(input("Enter a number to check if it is in the list: "))
    print(f"{check_num} is in the list is {check_num in my_list}")

    print("\nAssigning 'a' to 'c' (a = c)")
    c = a
    print(f"a: {a}, c: {c}")
    print(f"'a' and 'c' point to the same object is {a is c}")

 if __name__ == "__main__":
        main()
