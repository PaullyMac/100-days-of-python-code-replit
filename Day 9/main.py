print("Generation Identifier")
print()

year = int(input("Which year were you born? "))

if year >= 1883 and year <= 1900:
    print("Hah! Lost Generation! Avocado toast and Starbucks much!")
elif year >= 1901 and year <= 1927:
    print("Hah! Greatest Generation! Avocado toast and Starbucks much!")
elif year >= 1928 and year <= 1945:
    print("Hah! Silent Generation! Avocado toast and Starbucks much!")
elif year >= 1946 and year <= 1964:
    print("Hah! Baby Boomers! Avocado toast and Starbucks much!")
elif year >= 1965 and year <= 1980:
    print("Hah! Generation X! Avocado toast and Starbucks much!")
elif year >= 1981 and year <= 1996:
    print("Hah! Millennials! Avocado toast and Starbucks much!")
elif year >= 1997 and year <= 2012:
    print("Hah! Generation Z! Avocado toast and Starbucks much!")
elif year >= 2013 and year <= 2024:
    print("Hah! Generation Alpha! Avocado toast and Starbucks much!")
else:
    print("Year not recognized!")