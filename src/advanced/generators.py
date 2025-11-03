# A generator is a special type of iterator that yields values one at a time and maintains its state between calls.
# They are more memory efficient than lists for large datasets since they generate values on the fly.
def generator():
    yield 1
    yield 2
    yield 3


gen = generator()

for value in gen:
    print(value)

another_gen = generator()

print(next(another_gen))
print(next(another_gen))
print(next(another_gen))

sum_of_values = sum(generator())
print("Sum of values from generator:", sum_of_values)
