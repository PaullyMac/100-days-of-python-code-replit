print("Exam Grade Calculator")
print()
input("Name of exam: ")
print()
maxScore = float(input("Max. Possible Score: "))
print()
yourScore = float(input("Your score: "))
print()
percentage = round((yourScore / maxScore) * 100, 2) 

if percentage >= 90:
  print("You got", percentage, "% which is an A+")
elif percentage >= 80:
  print("You got", percentage, "% which is an A-")
elif percentage >= 70:
  print("You got", percentage, "% which is a B")
elif percentage >= 60:
  print("You got", percentage, "% which is a C")
elif percentage >= 50:
  print("You got", percentage, "% which is a D")
elif percentage >= 40:
  print("You got", percentage, "% which is a U")
else:
  print("You got", percentage, "% which is a F")