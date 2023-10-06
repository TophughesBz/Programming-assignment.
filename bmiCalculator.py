def calculate_bmi(mass_kg, height_metres):
    bmi = mass_kg / pow(height_metres,2)
    return bmi

def interpretation(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    else:
        return "Overwight"
mass_kg = float(input("Enter weight in kilograms :"))
height_metres = float(input("Enter your height in metres :"))
bmi = calculate_bmi(mass_kg, height_metres)
bmi = round(bmi,2)
bmiCategory = interpretation(bmi)
print("Your bmi is " + str(bmi) +" which is category "+ interpretation(bmi))