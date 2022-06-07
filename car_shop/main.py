import os


class Car:
    """ This Class represents the Cars that are purchasable """

    def __init__(self, make, color, qty):
        """ initialize the Cars with specific make, color and Quantity """

        global LOT
        self.make = make
        self.color = color
        self.qty = int(qty)

        # adding the new Car to the Lot
        LOT.append([make, color, int(qty)])


def cls():
    """ This Function always clears the Terminal"""

    os.system('cls' if os.name == 'nt' else 'clear')


def sell_cars():
    """ This is the Mainloop to sell the Cars until the Lot is Empty"""

    global LOT
    total = 1

    # running the Shop until somebody exits it or the Lot is Empty
    while total > 0:

        # generating the Total amount of available Cars
        total = sum([x[2] for x in LOT])
        if total == 0:
            break

        answer = "x"
        # asking the User if he wants to buy a Car
        while answer.lower() not in ["y", "n"]:
            answer = input(f"We have {total} cars in the lot, Would you like to buy one?(y/n): ")

        if answer.lower() == "y":

            # creating Variable for the Car-Number
            # (the Number the User has to enter for a specific Car)
            car_number = 1

            # adding 0 for Exit as a possible Number
            nums = [0]

            # generate the Car-List with all available Cars
            cls()
            print("Which Car would you like to buy?\n\npress 0 to exit")
            for car in LOT:

                # List the Car only if it is in Stock
                if car[2] > 0:
                    print(f"press {car_number} for {car[1]} {car[0]} ({car[2]} left.)")
                    nums.append(car_number)
                    car_number += 1

            # Waiting for the User to pick a Car or Exit
            choice = int(input("\nInput: "))

            # if the Number is not valid ask again
            while choice not in nums:
                choice = int(input("Incorrect Choice. Please try again: "))

            # if the User picked a Car, buy it, let him know and restart the Shop
            if choice > 0:

                # lowering the Choice to match the Index of the Lot-Array
                c = choice - 1
                if LOT[c][2] > 0:

                    # lowering the amount of this Car in Stock
                    LOT[c][2] -= 1

                    # inform the User of the Purchase
                    cls()
                    print(f"You bought a {LOT[c][1]} {LOT[c][0]}.")
                else:
                    # if a Car got listed, but it is not available restart the loop
                    cls()
                    print(f"Sorry, we don't have any {LOT[c][1]} {LOT[c][0]} left.")

            # if the User picks Exit, quit the Shop
            if choice == 0:
                cls()
                print("Thanks for visiting CarsAutoShop")
                break
        # if the User picks No from the beginning quit the Shop
        else:
            cls()
            print("Thanks for visiting CarsAutoShop")
            break


# generate the empty Lot
LOT = []

# populate the Lot with Cars
Car("Toyota", "red", 2)
Car("Porsche", "blue", 10)
Car("Honda", "green", 5)

# start the Shop
sell_cars()
