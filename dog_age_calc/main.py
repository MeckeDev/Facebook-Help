def age_calc(d_age):

    try:
        d_age = float(d_age)
    except ValueError:
        return f"{d_age} is not a valid Number."

    if d_age > 0:
        if d_age <= 1:
            h_age = d_age*15
        elif d_age <= 2:
            h_age = d_age*12
        elif d_age <= 1:
            h_age = d_age*9.3
        elif d_age <= 1:
            h_age = d_age*8
        elif d_age <= 1:
            h_age = d_age*7.2
        else:
            h_age = 36+(d_age-5)*7

        return f"The given Dog age {round(d_age,2)} is {round(h_age,2)} in human Years."


print(age_calc(input("How old is your Dog?\nEnter age in Years: ")))
