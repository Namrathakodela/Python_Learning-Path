# Two Sum using Hash Map

numbers = [2, 7, 11, 15]
target = 9

seen = {}

for i, number in enumerate(numbers):

    complement = target - number

    if complement in seen:
        print("Indices:", seen[complement], i)
        break

    seen[number] = i