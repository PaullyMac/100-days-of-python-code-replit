print("MY LOGIN SYSTEM")
print("+++++++++++++++")
print("")


username = input("Username > ")
password = input("Password > ")

if username == "David" and password == "totallyNotBald":
    print("Why hello there David, what a lovely accent you have, you could have charmed your way in here even without a password.")
elif username == "Paul" and password == "paul":
    print("Have a great day!")
elif username == "Jack" and password == "jack":
    print("Don't forget to wear a hat in the sun!")
else:
    print("Go away!")