import random

print("a random in 0 1 range:", random.random())
print("a random integer:", random.randint(1, 100))
print("a random choice:", random.choice(["apple", "banana", "cherry"]))
print("a random sample:", random.sample(range(1, 100), 5))
a_list = [1, 2, 3, 4, 5]
random.shuffle(a_list)
print("shuffling a list:", a_list)
