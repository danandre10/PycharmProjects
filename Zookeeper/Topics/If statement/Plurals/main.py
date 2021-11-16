number = int(input())
word = input()

# write a condition for plurals
plural_form = 's'
if number > 1 or number == 0:
    word += plural_form  # Avoiding Explicit Concatenation

print(number, word)
