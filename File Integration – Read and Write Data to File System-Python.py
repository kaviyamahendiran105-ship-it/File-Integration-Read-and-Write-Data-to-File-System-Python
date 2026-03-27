# File Integration - Read and Write

# Write to file
file = open("student.txt", "w")
data = input("Enter student details: ")
file.write(data)
file.close()

# Read from file
file = open("student.txt", "r")
content = file.read()
print("\nStored Data:")
print(content)
file.close()

# Append to file
file = open("student.txt", "a")
more_data = input("\nEnter more details to append: ")
file.write("\n" + more_data)
file.close()

# Read again
file = open("student.txt", "r")
print("\nUpdated Data:")
print(file.read())
file.close()
