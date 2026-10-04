# *args and **kwargs

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))


def student_details(**details):
    for key, value in details.items():
        print(key, ":", value)


student_details(
    name="Namratha",
    age=21,
    branch="CSE",
    college="BTech"
)