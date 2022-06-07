""" Module to calculate the Windchill """
while True:

    try:
        temp = float(input("What is the Temperature? "))
        unit = input("Fahrenheit or Celsius (F/C)? ")

        if unit.lower() == "c":
            temp = round((temp * 9/5) + 32)

        for i in range(5,65,5):

            wind_chill = round(35.74 + temp*0.6215 - 35.75*(i**0.16) + temp*0.4275*(i**0.16), 2)
            print(f"At temperature {temp}°F, and wind speed {i} mph, "
                  f"the windchill is: {wind_chill} °F")

    except ValueError:
        print("Please only user Numbers.")
