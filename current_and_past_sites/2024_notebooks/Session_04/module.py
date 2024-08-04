def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This block will only run when module.py is executed directly.
    name = input("Enter your name: ")
    print(greet(name))