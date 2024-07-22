print("Tip Calculator")
print()

myBill = float(input("How much did you spend? "))

tip = int(input("What percentage do you want to tip? "))

numberOfPeople = int(input("How many people in your group? "))

answer = myBill / numberOfPeople
tip1 = tip / 100
tip2 = round(tip1,2) * round(answer,2)

print("You each owe", round(answer,2) + round(tip2,2))