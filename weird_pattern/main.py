# user can input the Width of the Square
width = int(input("Width: "))

# user can input the Height of the Square
height = int(input("Height: "))

# this generates the first row of Stars
output = ("*" * width) + "\n"

# here we add each row with the ! Signs
for i in range(height-2):
    output += "!" + (" " * (width -2)) + "!\n"

# we end the Output with another line of Stars
output += "*"  * width

#print the Output to the Console
print(output)