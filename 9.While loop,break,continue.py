i=1
while i<=5:
    print(i)
    i+=1


is_failed=True
i=1
while is_failed:
    if i%2!=0: #not even
        i=i+1
        continue
    print(f"Attempt {i}")
    i=i+1
    if i>100:
        break
print("I gave up")



i=10
while i<=10:
    x=0
    while x<i:
        print("pragathi", end="-")
        x+=1
    print("")
    i+=1



pin="1234"
input_pin=input("PIN:")
while trials<=3:
    input_pin==input(f"trial-{trials} | pin:")
    trials+=1
    if input_pin==pin:
        print("correct")
    else:
        print("incorrect")


