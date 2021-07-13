while True:
    try:
        binary = input("Please enter a binary Number: ")
        new_bin = []
        decimal = 0
        power = 1

        if binary == "exit":
            break

        for i in binary:
            if i in ["0","1"]:
                new_bin.append(int(i))
            else:
                raise ValueError
        
        new_bin = new_bin[::-1]

        for i in new_bin:
            decimal += i*power
            power *= 2

        print(f"The Number {binary} is {decimal} in Decimal")

    except ValueError:
        print("Please only enter binary Numbers.")

