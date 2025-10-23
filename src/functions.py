def greet_command(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

def greet_query(first_name, last_name, greeting="Hello"):
    return f"{greeting}, {first_name} {last_name}!"

def multiply(*args):
    result = 1
    for number in args:
        result *= number
    return result

greet_command("John", "Doe")
greet_command(first_name="Alice", last_name="Johnson")
print(greet_query("Jane", "Smith", "Hi"))
print(f"Using a variable number of arguments: 2*3*4 = {multiply(2, 3, 4)}")