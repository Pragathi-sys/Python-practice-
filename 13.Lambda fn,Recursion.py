#Functionas - Advanced concept

def add(*num):
    return sum(num)
print(add(1,2,3,4,5))


#*args
def total_sum(*numbers):
    result=0
    for num in numbers:
        result+=num
    return result
print(total_sum(1,2,3,4))


#**kwargs
def student_info(**details):
    for key, value in details.items():
        print(f"{key}:{value}")
student_info(name="pragathi", age="22", course="python")


#lambda functions  (annonymous function)
add = lambda a,b : a+b
print(add(1,2))

double= lambda x : 2*x
print(double(200))


#lambda using dict in list
students=[
    {"name":"pragathi", "marks":80},
    {"name":"vasudha", "marks":75},
    {"name":"vidhya", "marks":85}
]
students.sort(key = lambda x: x["marks"], reverse=True)
print(students)


#recursion
def factorial(n):
    if n==1:
        return 1
    return n* factorial(n-1)
print(factorial(3))

#nested function
def calculate(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    def div():
        print(a/b)
    add()
    sub()
    mul()
    div()
calculate(10,20)