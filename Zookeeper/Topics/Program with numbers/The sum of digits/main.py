# put your python code here

number = int(input())

third_digit = number % 10  # Last digit will be here. Will use it for the final sum.
two_digit_number = number // 10  # the first two digits will be here.
second_digit = two_digit_number % 10  # Second digit will be here. Will use it for the final sum.
first_digit = two_digit_number // 10  # First digit will be here. Will use it for the final sum.

sum_digits = first_digit + second_digit + third_digit
print(sum_digits)
