def greet_command(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


def greet_query(first_name, last_name, greeting="Hello"):
    return f"{greeting}, {first_name} {last_name}!"


def multiply(*args):
    result = 1
    for number in args:
        result *= number
    return result


def using_all_kind_of_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


def enforcing_keyword_only_args(*, mandatory_kwarg):
    print(f"Mandatory keyword-only argument received: {mandatory_kwarg}")


greet_command("John", "Doe")
greet_command(first_name="Alice", last_name="Johnson")
greet_command(*["Bob", "Brown"])
greet_command(*("Carla", "Davis"))
greet_command(**{"first_name": "Eve", "last_name": "White"})
print(greet_query("Jane", "Smith", "Hi"))
print(f"Using a variable number of arguments: 2*3*4 = {multiply(2, 3, 4)}")
using_all_kind_of_args(1, 2, 3, a=4, b=5)
enforcing_keyword_only_args(mandatory_kwarg="This is required")
