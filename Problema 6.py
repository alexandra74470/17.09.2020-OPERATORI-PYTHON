n=1945
a=n%1000%100%10//1
print(a)
b=n%1000%100//10
print(b)
c=n%1000//100
print(c)
d=n//1000
print(d)
print(a,b,c,d)
print("suma","=", a+b+c+d)
print("restul impartirii","=", n%9)
print("catul impartirii","=", n//9)