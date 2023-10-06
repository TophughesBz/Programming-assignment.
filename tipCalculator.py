def calculate_tip(totalBill,tipPercentage,numPeople):
    tip =totalBill * (tipPercentage/100)
    totalPayment = totalBill + tip
    per_person_split = totalPayment / numPeople
    return per_person_split

totalBill = float(input("Enter the total bill amount :"))
tipPercentage = float(input("Enter tip percentage :"))
numPeople = int(input("Enter the number of people splitting the bill :"))

per_person_split = calculate_tip(totalBill,tipPercentage,numPeople)
per_person_split = round(per_person_split,2)

print("Each person should pay :$" + str(per_person_split))