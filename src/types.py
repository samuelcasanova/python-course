x = "1"
x_as_int = int(x)
x_as_float = float(x)
x_as_str = str(x_as_int)
x_as_bool = bool(x_as_int)

print("x as int:", x_as_int)
print("x as float:", x_as_float)
print("x as str:", x_as_str)
print("x as bool:", x_as_bool)
print("Type of x_as_str:", type(x_as_str))

print("Falsy values:")
print("bool(0):", bool(0))
print("bool(""):", bool(""))
print("bool([]):", bool([]))
print("bool(None):", bool(None))