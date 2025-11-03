def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function.")
        func(*args, **kwargs)
        print("After calling the function.")
    return wrapper


def repeater_decorator(num_repeats=1):
    def my_repeater_decorator_inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_repeats):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return my_repeater_decorator_inner


@debug_decorator
@repeater_decorator(num_repeats=3)
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Alice")
