s = input()
result = ""

for char in s:
    if not char.isdigit():
        result += char

print(result)