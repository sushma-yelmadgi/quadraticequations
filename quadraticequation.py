import cmath
a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))
if(a>0):
    d=(b**2)-(4*a*c)
    sol1=(-b-cmath.sqrt(d))/(2*a)
    sol2=(-b+cmath.sqrt(d))/(2*a)
else:
    print('a is negative value')
print('Quadratic equation',sol1,sol2)
