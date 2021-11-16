word_one = input()
word_two = input()

# How many letters does the longest word contain?
if len(word_one) > len(word_two):
    print(len(word_one))
else:
    print(len(word_two))
