class ValueTooStrangeError(Exception):
    pass


class ValueTooNormalError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def raise_exception(condition):
    if condition:
        raise ValueTooStrangeError("An error occurred due to the condition being True.")
    else:
        raise ValueTooNormalError("The condition was False, which is considered too normal.", condition)


def assert_condition(condition):
    assert (condition), "Assertion failed: condition is False."


def try_except_example():
    try:
        raise_exception(True)
    except ValueError as e:
        print("Caught an exception:", e)
    except AssertionError as e:
        print("Caught an assertion error:", e)
    except Exception as e:
        print("Caught a general exception:", e)
    else:
        print("No exceptions were raised.")
    finally:
        print("Execution of try-except block is complete.")


try_except_example()
