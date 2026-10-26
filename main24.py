s = input().upper()

letters = {}

for char in s:
    if char >= "A" and char <= "Z":
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

maximum = max(letters.values())

result = ""

for char in sorted(letters):
    if letters[char] == maximum:
        result += char

print(result)
print(maximum)