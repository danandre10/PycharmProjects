# put your python code here
class_1 = int(input())
class_2 = int(input())
class_3 = int(input())

students_per_desk = 2  # Avoiding Magic Number

# Total Desks Class 1
desks_class_1 = class_1 // students_per_desk
remainder_class_1 = class_1 % 2
total_desks_class_1 = desks_class_1 + remainder_class_1

# Total Desks Class 2
desks_class_2 = class_2 // students_per_desk
remainder_class_2 = class_2 % 2
total_desks_class_2 = desks_class_2 + remainder_class_2

# Total Desks Class 3
desks_class_3 = class_3 // students_per_desk
remainder_class_3 = class_3 % 2
total_desks_class_3 = desks_class_3 + remainder_class_3

# Sum
total_desks = total_desks_class_1 + total_desks_class_2 + total_desks_class_3
print(total_desks)
