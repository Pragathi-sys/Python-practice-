name="pragathi"
for index,letter in enumerate(name):
    print(letter*(index+1))

cities=["benglore","mysure","hubli","manglore"]
for city in cities:
    if city=="hubli":
        print(f"found {city}")
        break
    print(city)



cities=["benglore","mysure","hubli","manglore"]
for city in cities:
    if city=="hubli":
        continue
    print(city)




for i in range(2,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")