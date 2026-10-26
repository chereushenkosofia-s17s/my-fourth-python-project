s = input()

upper = 0
lower = 0
spaces = 0

for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char == " ":
        spaces += 1

print("Upper", upper)
print("Lower", lower)
print("Spaces", spaces)