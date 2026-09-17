l=[10,14,15,18,19,13,12]
total=0
for num in l:
    print(total)
    total=total+num
print(total)


l=[10,14,15,18,19,13,12]
dl=[]
for num in l:
    dl.append(num*2)
    print(dl)


students={"A":85,"B":90,"C":70}
for students,marks in students.items():
    print(f"{students}--{marks}")


students=["A","B","C"]
marks=[80,90,95]
student_marks={}
for index,students in enumerate(students):
    student_marks[students]=marks[index]
print(student_marks)


students=["A","B","C"]
marks=[80,90,95]
student_marks={}
for i in range(1,len(students)):
    student_marks[students[i]]=marks[i]
print(student_marks)


l=[1,2,3,4,5]
#dl=[exp for iten in collection]
dl=[item*2 for item in l] 
print(dl)

l=[x for x in range(1,11)]
print(l)
dl=[x**2 for x in l]
print(dl)


#list comprehension
l=[x for x in range(1,11)]
print(l)
evendl=[x**2 for x in l if x%2==0]
print(evendl)

l=["pragathi","saniya","ashiqa"]
print(l)
cl=[x[1] for x in l]
print(cl)

#dictionary comprehension
names=["pragathi","saniya","ashiqa"]
d={name:len(name) for name in names}
print(d)

cp={
    "banglore":80,
    "mysure":50,
    "hubli":11,
    "udpi":5
}
lc={key:value for key,value in cp.items() if value>40}
lc={city:pop for city,pop in cp.items() if pop>40}
print(lc)

#splitting strings to create lists
s="this is a computer"
l=s.split()
print(l)

print("list input practice")
x=input("enter list of integer:")
print(x.split())

print("list input practice")
x=input("enter list of integers:").split()
l=[int(num) for num in x]
print(l)

