def calculate_age(birthMonth,birthDay,currentMonth,currentDay):

    if(birthMonth > currentMonth):
        ageMonth =birthMonth - currentMonth
    else:
        ageMonth =currentMonth - birthMonth

    if(birthDay> currentDay):
        ageDay = birthDay -currentDay
    else:
        ageDay = currentDay - birthDay
    return ageDay,ageMonth

birth_year=int(input("Enter your birth year :"))
birthMonth=int(input("Enter your birth month :"))
birthDay=int(input("Enter your birth day :"))

currentYear=2023
currentMonth=10
currentDay=6
ageYear = currentYear - birth_year


ageMonth,ageDay =calculate_age(birthMonth,birthDay,currentMonth,currentDay)


print("Your age is {} years, {} months, and {} days old".format(ageYear, ageMonth, ageDay))
