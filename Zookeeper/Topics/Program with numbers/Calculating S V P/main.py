# put your python code here
length = int(input())
width = int(input())
height = int(input())

sum_edge_length = 4 * (length + width + height)
surface = 2 * ((length * width) + (width * height) + (length * height))
volume = length * width * height

print(sum_edge_length)
print(surface)
print(volume)
