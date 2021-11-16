# put your code here
number = int(input())

# Variables
stops = 55
counting = 0
total_sum = 0
average = 0

while number != stops:
    counting += 1
    total_sum += number
    number = int(input())
average = round(total_sum / counting)

print(counting)
print(total_sum)
print(average)
