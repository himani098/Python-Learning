name = input("Enter your name: ")
name = name.capitalize()
name = name.strip().title()
print("Hello, " + name)
print("Hello,", name)

print("Hello, ", end="")
print(name)

print(f"Hello, {name}")

first, last = name.split(" ")
print(f"Hello, {first}")