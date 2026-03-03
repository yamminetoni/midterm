import random

random_numbers = []

# create list of 10 random numbers between 1 and 100
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# go through the list and modify values
for i in range(len(random_numbers)):

    # if number is greater than 80, replace with negative value
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]

    # if number is lower than 40, replace with sum of its digits
    elif random_numbers[i] < 40:
        number = random_numbers[i]
        digit_sum = 0

        # calculate sum of digits
        while number > 0:
            digit_sum = digit_sum + (number % 10)
            number = number // 10

        random_numbers[i] = digit_sum

# print final list
print(random_numbers)