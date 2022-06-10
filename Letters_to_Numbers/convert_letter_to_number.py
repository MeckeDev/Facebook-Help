""" Module to convert Letters to Numbers """


def convert_to_number(user_input):
    """ converts a Letter to a Number """

    letters = {
        "A": 4,
        "B": 3,
        "C": 2
    }
    """ Dictionary to translate Letters to Numbers """

    new_value = [str(letters[x.upper()])
                 if x.upper() in letters
                 else "-INVALID-"
                 for x in user_input.replace(" ", "").split(",")
                 ]
    """ generating a List of Numbers for each Letter we have sent """

    #  returning a String containing all Numbers we have converted
    return ", ".join(new_value)


#  getting User-Input containing Letters to convert
user = input("Enter your Letter: ")

#  printing the Results
print(convert_to_number(user))
