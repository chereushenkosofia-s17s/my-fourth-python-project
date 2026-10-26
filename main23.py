s = input()

result = 0
number = ""
sign = 1

for char in s:
    if char.isdigit():
        number += char
    else:
        result += sign * int(number)
        number = ""

        if char == "+":
            sign = 1
        else:
            sign = -1

result += sign * int(number)

print(result)