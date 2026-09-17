x=24
if x%2==0:
    print("x is even")
else:
    print("x is odd")



signal="green"
if signal=="red":
    print("stop")
elif signal=="yellow":
    print("ready")
else:
    print("go")


signal=input("enter colour of signal: ")
if signal=="red":
    print("stop")
elif signal=="yellow":
    print("ready")
elif signal=="green":
    print("go")
else:
    print("there is no colour")



gender=input("enter gender:")
age=int(input("enter age:"))
if gender=="female":
    print("ticket is free")
else:
    if age<5:
        print("ticket is free")
    elif age<=12:
        print("child discount")
    elif age>=60:
        print("citizen discount")
    else:
        print("full fare")