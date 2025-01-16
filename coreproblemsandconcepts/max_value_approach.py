array = [4, 7, 5, 9, 2]
max = float('-inf')

for item in array:
    if item > max:
        max = item

print(f"Max is {max}")
