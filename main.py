print ("Year to Seconds Converter")

print()

year = int(input("Enter the year: "))
print()
if year % 4 == 0:
  yeartodays = 1 * 365
  yeartohours = yeartodays * 24
  yeartominutes = yeartohours * 60
  yeartoseconds = yeartominutes * 60
  print("There are", yeartoseconds, "seconds in the year", year)
else:
  yeartodays = 1 * 366
  yeartohours = yeartodays * 24
  yeartominutes = yeartohours * 60
  yeartoseconds = yeartominutes * 60
  print("There are", yeartoseconds, "seconds in the year", year)