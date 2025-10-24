single_line_string = "This is a single line string."
print(single_line_string)

very_long_string = """
This is a very long string that spans
multiple lines for demonstration purposes.
It helps to show how triple quotes work in Python.
"""
print(very_long_string)

print("Long string length:", len(very_long_string))

print("Escaping a quote: He said, \"Hello!\"")
print("Including\nline\nbreaks")

name = "Alice"
print("Alice's first character is:", name[0])
print("Alice's last character is:", name[-1])
print("Substring from index 1 to 3:", name[1:4])
print("Alice from the 3rd character to the end:", name[2:])
print("Alice excluding the first and last character:", name[1:-1])
print("Alice string copy:", name[:])

surname = "Smith"
print("Formatted string with expressions:", f"{name} {surname} and the number { 1 + 2 + 3 }")

print("Using string methods:")
print(" this is a sample text ".upper().lower().strip().capitalize().ljust(20))