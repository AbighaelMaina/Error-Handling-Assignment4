# Start with an empty list
my_list = []

# Add numbers to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Add 15 at the second position (index 1)
my_list.insert(1, 15)

# Add more numbers to the end of the list
my_list.extend([50, 60, 70])

# Remove the last number from the list
my_list.pop()

# Arrange the numbers from smallest to biggest
my_list.sort()

# Find where 30 is in the list
index_of_30 = my_list.index(30)

# Show the position of 30
print("30 is at position:", index_of_30)
