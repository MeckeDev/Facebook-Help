width = int(input("Width: "))
height = int(input("Height: "))

output = ("*" * width) + "\n"

for i in range(height-2):
    output += "!" + (" " * (width -2)) + "!\n"

output += "*"  * width

print(output)