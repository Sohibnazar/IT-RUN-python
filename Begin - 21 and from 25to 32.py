#begin-21
def triangle_1(a,b,c):
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    print("P= "+str(p)+ "  S= "+str(round(area,2)))
triangle_1(2,3,4)
#begin -25
def func(x):
    y=3*x**6-6*x**2-7
    print("Y= "+str(y))
func(3)
#begin -26
def func_1(x):
    y= 4*(x-3)**6-7*(x-3)**3+2
    print("Y= "+str(y))
func_1(3)
#begin-27
def chislo(A):
    A2=A*A
    A4=A2*A2
    A8=A4*A4
    print("A2= "+str(A2)+" A4= "+str(A4)+" A8="+str(A8))
chislo(4)

#begin-28
def chislo_1(A):
    A2=A*A
    A3=A2*A
    A5=A3*A2
    A10=A5*A5
    A15=A10*A5
    print("A2= "+str(A2)+" A3= "+str(A3)+" A5="+str(A5)+"  A10= "+str(A10)+ " A15="+str(A15))
chislo_1(4)
#begin-29
def radian(x,PI=3.14):
    rad=(x*PI)/180
    print( "60 градус= "+str(round(rad,2) ))
radian(60)

#begin-30
def radian_1(x,PI=180):
    radi=(x*180)/PI
    print( "60 радиан= "+str(round(radi,2))+"градус")
radian_1(60)

#begin-31
def fare(Tf):
    Tc=(Tf-32)*5/9
    print(str(Tf)+" Фаренгейт равен "+str(round(Tc,2)))
fare(54)

#begin-32
def fare_2(Tc):
    Tf=Tc*9/5+32
    print(str(Tc)+" целсий равен "+str(round(Tf,2)))
fare_2(54)





