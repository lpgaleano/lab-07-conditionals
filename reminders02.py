import datetime


#user.time = float(input("what hour is it? (0-23)"))
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)


if now.hour <= 5:
    print("its early you should be sleeping!")
elif now.hour <= 7:
    print("wake up, make coffe, run a mile and get bfest")
elif now.hour <= 9:
    print("Time to Work")
elif now.hour <= 12:
    print("keep working")
elif now.hour <= 13:
    print("Take your lunch break")
elif now.hour <= 17:
    print("Do you feel that afternoon lull")
elif now.hour <= 19:
    print("Time to hit the gym")
elif now.hour <= 21:
    print("Gotta eat that dinner")
elif now.hour <= 23:
    print("Go to bed !")
else:
    print("you didnt type and acceptable value (0-23)")
