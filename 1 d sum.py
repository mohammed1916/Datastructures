def sumIterative(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def sumRecursive(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sumRecursive(numbers[1:])

print("The sum for numbers [1, 2, 3, 4, 5] calculated iteratively is: ",sumIterative([1, 2, 3, 4, 5]))

print("The sum for numbers [1, 2, 3, 4, 5] calculated recursively is: ",sumRecursive([1, 2, 3, 4, 5]))
# output 15