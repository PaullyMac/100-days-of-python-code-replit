exit = ""

while exit != "yes":
    animal = input("What animal do you want? ")

    if animal == "cow":
        print("A cow goes moo.")
    elif animal == "dog":
        print("A dog goes woof.")
    elif animal == "cat":
        print("A cat goes meow.")
    elif animal == "sheep":
        print("A sheep goes baa.")
    elif animal == "pig":
        print("A pig goes oink.")
    elif animal == "horse":
        print("A horse goes neigh.")
    elif animal == "chicken":
        print("A chicken goes cluck.")
    elif animal == "duck":
        print("A duck goes quack.")
    elif animal == "Lesser Spotted Lemur":
        print("Ummm...the Lesser Spotted Lemur goes awooga.")
    else:
        print("I don't know that animal.")

    exit = input("Do you want to exit? ")