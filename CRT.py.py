"""n=12467
while n>0:
    print(n%10)
    n=n//10"""


"""n=5
while n>0:
    print(n)
    n=n-1"""

"""n=int(input("n="))
sum=0
while n>0:
    d=n%10
    n=n//10
    sum=sum+d
print(sum)"""


"""n=int(input("n="))
num=0
while n>0:
    n=n//10
    num=num+1
print(num)
"""


"""n=int(input("n="))
num=0
while n>0:
    d=n%10
    if d%2==0:
        num=num+1
    n=n//10
print(num)"""


"""n=int(input("n="))
sum=0
while n>0:
    n%r==0
print(r)
"""

"""n=int(input("n="))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s>n:
    print("true")
else:
    print("false")""" 


"""n=int(input("n="))
sum=0
n1=n
while n>0:
    d=n%10
    n=n//10
    sum=sum+d
if n1%sum==0:
    print("divisible")
else:
    print("not divisible")"""


"""n=int(input("n="))
num=0
n1=n
org=n
while n>0:
    n=n//10
    num=num+1
sum=0
while n1>0:
    d=n1%10
    sum=sum+d**num
    n1=n1//10
if sum==org:
    print("yes")
else:
    print("no")"""




#palindrome

"""n=int(input("n="))
r=0
n1=n
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
print(r)
if r==n1:
    print("palindrome")
else:
    print("not")"""



##list

"""list=[1,2.22,1,10,True,"hello"]
list.append("prasanth")
list.insert(3,"dinesh")
print(list)
for i in list:
    print(i)
for i in range(0,len(list)):
    print(list[i])
print(list[2])
print(list[::2])
print(list[2::3])
print(list[:2])
list[3]="hari"
print(list)"""


##tuplle

"""tuple=("hi","hello","world",12,14,2.11,True)
print(tuple)
tuple=tuple+("good",)
print(tuple)
tuple=tuple+(2.123456,"sss")
print(tuple)
for i in range(0,5):
    n=int(input("enter"))
    tuple=tuple+(n,)
    print(tuple)"""


"""list=[42,36,28,96,4,-1,1]
mini=999
maxi=-999
for i in range(0,len(list)):
    if list[i]<mini:
        mini=list[i]
    if list[i]>maxi:
        maxi=list[i]
print(mini+maxi)"""




#dictonary

"""dict={1:"hi",
      2:"hey",
      3:"hello",
      4:"bye" }
dict[4]="byeeeee"
print(dict)
dict[5]="okay"
print(dict)
print(dict[4])

for i in dict:
    print(i)
for i in dict.values():
    print(i)
for x,y in dict.items():
    print(x,y)
dict.pop(1)
print(dict)"""


"""l=[[11,21,31],["a","b","c"],[4.5,3.5]]
print(l[0][0])
print(l[0][1])
print(l[0][2])
print(l[1][0])
print(l[1][1])
print(l[1][2])
print(l[2][0])
print(l[2][1])
print(l[0][1])"""



#set

"""set={10,20,30,40}
print(set)
set.add(50)
print(set)
set.update([60,70,80,90])
print(set)
set.discard(10)
print(set)
set.remove(50)
print(set)
set.pop()
print(set)
set2={10,20,30,40,110,120,55}
new=set.union(set2)
print(new)
new=set.intersection(set2)
print(new)
new=set.difference(set2)
print(new)"""


#functions

"prime number"

"""def prime():
    f=1
    num=int(input("enter a number="))
    for i in range(2,num):
        if num%i==0 :
            f=0
            break
    if f==0:
        print("not prime")
    else:
        print(" prime")
prime()"""


"""a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))
def x(a,b,c):
    z=a+b+c
    print(z/3)
x(a,b,c)"""



#LOGIN PAGE(3 models)
"""def login():
    n=1
    while n!=0:
        username=input("enter username=")
        password=input("enter password=")
        if username==password:
            print("login successful")
            n=0
        else:
            print("invalid")
login()"""

"""def login():
    n=1
    while n!=0:
        username=input("enter username=")
        password=input("enter password=")
        if username==password:
            print("login successful")
            break
        else:
            print("invalid")
login()"""

"""def login():
    while True:
        username=input("enter username=")
        password=input("enter password=")
        if username==password:
            print("login successful")
            break
        else:
            print("invalid")
login()"""


#recursion


""""factorial"""

"""n=5
def f(n):
    if n==0:
        return 1
    return n*f(n-1)
a=f(5)
print(a)"""

"""fibonacci series"""

"""n=5
def f(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return f(n-1)+f(n-2)
a=f(n)
print(a)"""

#power
"""def f(m,n):
    m=int(input("enter m="))
    n=int(input("enter n="))
    if n==0:
        return 1
    return m*f(m,n-1)
a=f(m,n)
print(a)"""


"""n= int(input("enter n = "))
def check(n):
    if n%10==5:
        return n**2
    elif n%10==3:
        return n**3
    elif n%10==6:
        return n-1
    else:
        return n/2
a=check(n)
print(a)"""


#Oops

"""class f15:
    def light(self):
        print("light is on")
    def fan(self):
        print("fan is on")
    def cpu(self):
        print("cpu is on")
hello=f15()
hello.cpu()
hello.fan()"""


"""class f15:
    def light(self):
        print("light is on")
    def fan(self,speed):
        print("fan is on and the speed is",speed)
        self.s=speed
    def cpu(self):
        print("cpu is on")
        print(self.s)
hello=f15()
hello.light()
hello.fan(5)
hello.cpu()"""




"""class shopping:
    def dresstype(self,cate):
        print("type of dress user wants is ",cate)
        self.c=cate
    def price(self,range):
        print("price of the dress is ",range)
        self.r=range
    def size(self,fit):
        print("size of the dress is ",fit)
        self.f=fit
    def display(self):
        print(self.c,self.r,self.f)
        
bill=shopping()
bill.dresstype("shirt")
bill.price(2000)
bill.size("m")
bill.display()"""

"""constructor"""

"""class shopping():
    def __init__(self,place):
        self.place=place
        print("welcome to ",place)
    def dresstype(self,cate):
        self.c=cate
    def price(self,range):
        self.r=range
    def size(self,fit):
        self.f=fit
    def display(self):
        print(self.c,self.r,self.f)
        
bill=shopping("zara")
bill.dresstype("shirt")
bill.price(2000)
bill.size("m")
bill.display()"""

#INHERITANCE

"""multi level"""

"""class f15:
    def light(self):
        print("light is on")
f=f15()


class btech(f15):
    def bus(self):
        print("busses are started")
b=btech()


class city(btech):
    def hyd(self):
        print("hitech city")
c=city()
c.light()
c.hyd()
c.bus()"""




"""multiple"""

"""class f15:
    def light(self):
        print("light is on")
f=f15()


class btech:
    def bus(self):
        print("busses are started")
b=btech()


class city(f15,btech):
    def hyd(self):
        print("hitech city")
c=city()
c.bus()
c.light()
c.hyd()"""
        


"""hirerachial"""

"""class f15:
    def light(self):
        print("light is on")
f=f15()


class btech(f15):
    def bus(self):
        print("busses are started")
b=btech()


class city(f15):
    def hyd(self):
        print("hitech city")
c=city()

class room(f15):
    def bench(self):
        print("sit on the bench")
r=room()
f.light()
b.light()
b.bus()
c.light()
c.hyd()"""


"""class art:
    def add(self,a):
        print(a)
    def add (self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj=art()
obj.add(1,2,3)"""

"""class art:
    def __init__(self):
        print("there is no argument")
    def __init__(self,a):
        print("passing one argument")
    def __init__(self,a,b):
        print("passing two argument")
obj=art(2,2)"""
    


"""class car_showroom:
    def company(self,name):
        c=["landrover","mg","mahindra"]
        if name in c:
            print("welcome to ",name)
    def model(self,name):
        d={"landrover":["rangerover","defender"],"mg":["hector","gloster"],"mahindra":["thar","xuv"]}
        if name in d:
            print(d[name])
    def price(self,name,m):
        print("you have selected",m)
        price_list={"rangerover":20000000,"defender":15000000,"hector":3000000,"gloster":5000000,"thar":4000000,"xuv":3500000}
        if m in price_list:
            car_price=price_list[m]
            cgst=0.1*car_price
            sgst=0.1*car_price
            insurance=100000
            onroad_price=car_price+cgst+sgst+insurance
            print("onroad price:",onroad_price)
n=input("enter car company:") 
car=car_showroom()
car.company(n)
car.model(n)
m=input("enter model of car:")
car.price(n,m)"""
                   

class cars:
    def company(self):
        
        self.cgst=0.1
        self.sgst=0.1
        self.insurance=100000

        while True:
            print("select a car company mg or tata")
            self.n=input("enter car company")
            if self.n=="mg":
                print("welcome to mg")
                self.model()
                break
            elif self.n=="tata":
                print("welcome to tata")
                self.model()
                break
            else:
                print("select a valid car company")
    def model(self):
        if self.n=="mg":
            while True:
                print("select from hector and gloster")
                self.choice=input("enter tne car name ")
                if self.choice=="hector":
                    self.price(self.choice)
                    break
                elif self.choice=="gloster":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid car name")
        elif self.n=="tata":
            while True:
                print("select from nexon and punch")
                self.choice=input("enter a car name ")
                if self.choice=="nexon":
                    self.price(self.choice)
                    break
                elif self.choice=="punch":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid car name")
    def price(self,choice):

        if choice=="hector":
            self.p=3000000
        elif choice=="gloster":
            self.p=5000000
        elif choice=="nexon":
            self.p=1500000
        elif choice=="punch":
            self.p=1200000


        total=self.p+(self.cgst*self.p)+(self.sgst*self.p)+self.insurance
        print(total)
a=cars()
a.company()



        
            
        




        














        
    


    


    
    
        





















 









    





