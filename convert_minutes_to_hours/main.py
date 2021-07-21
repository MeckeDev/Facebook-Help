from math import *

while True:
    try:
        total_minutes = int(input("""
How many Minutes do you want to convert?
Enter 0 to exit the Program

>>> """))

        if total_minutes == 0:
            break

        hours = floor(total_minutes/60)
        minutes = total_minutes - hours * 60

        print(f"{hours} Hours and {minutes} Minutes")
    except:
        print("Please only enter Numbers.")
