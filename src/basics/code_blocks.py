print("\nIf statement:")
temperature = 23
thermometer_working = True
if temperature > 25 and thermometer_working:
    print("It's a hot day.")
elif temperature < 15 and thermometer_working:
    print("It's a cold day.")
else:
    print("It's a pleasant day.")
print("Enjoy your day!")

print("\nTernary operator:")
temperature = 23
have_beer = False
print("It's a hot day." if temperature > 25 or not have_beer else "It's a cold day." if temperature < 15 else "It's a pleasant day.")

print("\nChaining comparisons:")
temperature = 23
if 20 < temperature < 30:
    print("The weather is nice.")

print("\nFor loop with an else statement:")
successful = False
for i in range(2, 10, 2): # range is an iterable
    print(f"Attempt: {i} {i * "."}")
    if successful:
        print("Success!")
        break
else:
    print("Attempted all options without success.")

print("\nFor loop using a string, which is an iterable:")
for char in "Python":
    print(char)

print("\nFor loop using an iterable list:")
for language in ["Python", "Javascript", "Ruby"]:
    print(language)

print("\nWhile loop:")
number = 20
while number > 10:
    print(number)
    number -= 5