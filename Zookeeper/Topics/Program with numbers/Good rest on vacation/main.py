# put your python code here
duration = int(input())
food_cost_per_day = int(input())
flight_cost = int(input())
two_way_flight = 2  # Avoiding Magic Number
night_cost = int(input())
minus_last_night = 1

total_food_cost = food_cost_per_day * duration
total_flight_cost = flight_cost * two_way_flight
total_night_cost = night_cost * (duration - minus_last_night)

print(total_food_cost + total_flight_cost + total_night_cost)
