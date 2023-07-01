""" Tool to convert Binary Numbers into Decimal, until User writes exit """

# While Loop to let the User convert multiple Numbers
while True:

    # only executes if the User enters a binary Number
    try:

        # setting up some default Values
        binary = input("Please enter a binary Number: ")
        new_bin = []
        decimal = 0
        power = 1

        # closes the Program if User wants to exit
        if binary == "exit":
            break

        # checks every Digit of the given Number to validate it is binary
        # if the Number is not binary we raise a ValueError and ask for new Input
        for i in binary:
            if i in ["0", "1"]:
                new_bin.append(int(i))
            else:
                raise ValueError

        # reversing the Array of 1's and 0's
        new_bin = new_bin[::-1]

        # adding the Power of each position of the binary Number to the decimal Number
        for i in new_bin:
            decimal += i * power
            power *= 2

        # Outputs the decimal Result
        print(f"The Number {binary} is {decimal} in Decimal")

    # this Error gets raised if the Number was not binary
    except ValueError:
        print("Please only enter binary Numbers.")
