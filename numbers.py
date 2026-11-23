# Function 1: Calculate the sum
def get_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total

# Function 2: Calculate the mean (average)
def get_mean(numbers):
    total = get_sum(numbers)
    mean = total / len(numbers)

    return mean

# Function 3: Calculate the median and mode
def get_median_mode(numbers):
    sorted_numbers = sorted(numbers)

    # Find the median
    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 1:
        median = sorted_numbers[middle]
    else:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    # Find the mode
    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    highest_frequency = max(frequency.values())

    modes = []

    for number in frequency:
        if frequency[number] == highest_frequency:
            modes.append(number)

    # If all numbers occur equally often, there is no mode
    if highest_frequency == 1:
        modes = []

    return median, modes

# Our list of numbers
numbers = [2, 4, 4, 6, 8]

# Calling the functions
print("Sum:", get_sum(numbers))
print("Mean:", get_mean(numbers))

median, mode = get_median_mode(numbers)

print("Median:", median)
print("Mode:", mode)
