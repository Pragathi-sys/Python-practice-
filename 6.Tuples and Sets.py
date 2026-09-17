genders  = ("male","female","others")
genders[0]="male v2"
print(genders)



s={143,223,30}
print(s)

f={"apple","banana","cherry"}

f.add("orange")
f.remove("banana")
f.discard("banana")
f.discard("kivi")
f.pop()
f.clear()

print(f)



t1=(1,2,3,4,5)
t2=(6,7,8,9,2)
t3= t1 + t2
print(t3)


f1={"rambutan","peru","apple"}
f2={"mango","lychee","peru"}
f1.add("orange")
f2.add("banana")
f1.remove("peru")
f2.remove("lychee")
f1.discard("apple")
print(f1)
print(f2)


list=[1,2,3,4,5]
tuple=tuple(list)
set=set(list)
print(list)
print(tuple)
print(set)