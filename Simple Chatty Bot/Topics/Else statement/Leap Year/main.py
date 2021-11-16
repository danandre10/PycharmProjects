# put your python code here
year = int(input())
leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print("Leap" if leap_year else "Ordinary")
