min_sleep = int(input())
max_sleep = int(input())
sleep_hours = int(input())

if sleep_hours < min_sleep:
    print("Deficiency")
else:
    if sleep_hours >= min_sleep:
        if sleep_hours <= max_sleep:
            print("Normal")
        else:
            print("Excess")
