# put your python code here
time_1 = int(input())
time_2 = int(input())
time_3 = int(input())
time_4 = int(input())
time_5 = int(input())
time_6 = int(input())

# creating these variables to avoid magic number
hour_sec_conversion = 3600
min_sec_conversion = 60

hours = (time_4 - time_1) * hour_sec_conversion  # Difference of hours transformed in number of seconds
minutes = (time_5 - time_2) * min_sec_conversion  # Difference of minutes transformed in number of seconds
seconds = (time_6 - time_3)  # Difference in seconds

print(hours + minutes + seconds)  # Sum of all seconds between both times
