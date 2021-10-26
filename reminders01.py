usertime = float(input("what hour is it? (0-23)"))

if usertime <= 5:
    print("its early you should be sleeping!")
elif usertime <= 7:
    print("wake up, make coffe, run a mile and get bfest")
elif usertime <= 9:
    print("Time to Work")
elif usertime <= 12:
    print("keep working")
elif usertime <= 13:
    print("Take your lunch break")
elif usertime <= 17:
    print("Do you feel that afternoon lull")
elif usertime <= 19:
    print("Time to hit the gym")
elif usertime <= 21:
    print("Gotta eat that dinner")
elif usertime <= 23:
    print("Go to bed !")
else:
    print("you didnt type and acceptable value (0-23)")
