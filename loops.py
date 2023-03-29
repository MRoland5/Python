
a = 213
i = 0
while a>0:
    a=int(a/10)
    i=i+1
print(i)


i=100
while i>0:
    i=i-1
    print(i)



i=1
while i<100:
    i=i+1
    print(i)

i = 10
a=0
while a<100:
    a=a+1
    if a%i==0:
        print(a)

a=4
i=1
b=1
while i<a:
    i+=1
    b=b*i
print(b)

a=0
b=1
c=0
i=1
lenght=10
while i<=lenght:
    i=i+1
    print(a)
    c=a+b
    a=b
    b=c

a=123
reversed=0
n=a
c=0
while n!=0:
    c=n%10
    reversed=reversed*10+c
    n=int(n/10)
print(reversed)

a=1232
reversed=0
n=a
c=0
while n!=0:
    c=n%10
    reversed=reversed*10+c
    n=int(n/10)
if a==reversed:
    print("this is palidrome")
else:
    print("this isn't palidrome")
 
i=2
while i<100:
    i=i+2
    print(i)

inp=10
i=2
Prim=True
while i<inp:
    i=i+1
    if inp&i==0:
        Prim = False
        break

if Prim ==True:
    print("this number is Prim")
else:
    print("this number is not Prim")
    
#ez valamiert nekem nem jo 
IsPrime=False
max=100
a=3
b=2
while a<=max:
    a=a+1
    IsPrime=True
    while b<a:
        b=b+1
        if a%b==0:
            IsPrime=False
            break
    if IsPrime==True:
        print(a)

s = 1
n=123
i=1
while i<+n:
    i=i+1
    s=s+i
print(s)
