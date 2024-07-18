print("Wholesome Positivity Machine")

print()

name = input("Who are you? ")
print()
achieve = input("What do you want to achieve? ")
print()

scale = input("On a scale of 1 - 10 how do you feel today? (1: 🙁, 10: 🥳) ")

print()

if scale == "1":
  print("Hey", name, ", I know things seem tough right now. Remember that even small steps towards", achieve, "are significant. You have the strength to get through this!")
elif scale == "2":
  print("Hey", name, ", it’s okay to feel down sometimes. Just keep focusing on", achieve, "and take it one day at a time. You’re doing great!")
elif scale == "3":
  print("Hey", name, ", don’t be too hard on yourself. Progress towards", achieve, "might be slow, but every effort counts. Keep going!")
elif scale == "4":
  print("Hey", name, ", you're doing better than you think. Keep pushing towards", achieve, "and remember that it’s okay to take breaks when needed.")
elif scale == "5":
  print("Hey", name, ", you're halfway there! Stay positive and keep your eye on", achieve, ". You’ve got this!")
elif scale == "6":
  print("Hey", name, ", you're on the right track. Keep your focus on", achieve, "and celebrate the small wins along the way. Great job!")
elif scale == "7":
  print("Hey", name, ", you're doing well! Your efforts towards", achieve, "are paying off. Keep up the fantastic work!")
elif scale == "8":
  print("Hey", name, ", you’re in a good place! Keep that momentum going as you work towards", achieve, ". You're awesome!")
elif scale == "9":
  print("Hey", name, ", you’re almost at the top! Your enthusiasm for", achieve, "is inspiring. Keep shining!")
elif scale == "10":
  print("Hey", name, ", you’re on fire! Your positivity and energy towards", achieve, "are incredible. Keep being amazing!")
else:
  print("Hey", name, ", it seems like the scale you entered is outside the range of 1 to 10. Please choose a number within that range to express your feelings.")