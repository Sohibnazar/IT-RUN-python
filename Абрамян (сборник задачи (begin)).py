
#Begin-1
print("Begin 1")
print ("""          =================
               P=4*a
          =================""")
a= int(input("   Вводите сторона квадрата: "))
p= 4*a
print("  Периметр квадрата равен: "+ str(p))

#Begin-2
print("Begin 2")
print("""          ================
              S=a*a
          ================""")
a= int(input(" Введите сторона квадрата: "))
S=a*a
print(" Площадь квадрата: " + str(S))

#Begin-3
print("Begin 3")
print("""          ================
              S=a*b, P=2*(a+b)
          ================""")
a= int(input(" Введите длина прямоугольника:"))
b=int(input(" Введите ширина прямоугольника:"))

A=a*b
D=2*(a+b)
print(" Площадь прямоугольника: "+ str(A))
print("  Периметр прямоуголтника :"+ str(D))
#Begin-4
print("Begin 4")
print("""          ================
               L=PI*d, PI=3.14
          ================""")
d=int(input("Введите диаметр окружность: "))
PI=3.14
L=PI*d
print ("Длина окружноста равен: "+str(L))
#Begin - 5
print("Begin 5")
print ("""            ===============
             V=a*a*a
            =================""")
a= int(input("Введите ребро куба: "))
V=a*a*a
print("Объема куба равен: "+str(V))
#Begin-6
print("Begin 6")
print ("""            ===============
             V=a*b*c; S=2*(a*b+b*c+a*c)
            =================""")
a= int(input("Введите ребро параллелепипеда: "))
b= int(input("Введите ребро параллелепипеда:"))
c=int(input("Введите ребро параллелепипеда:"))
V=a*b*c
S=2*(a*b+b*c+a*c)
print("Объем параллелепипеда: "+ str(V))
print(" Площади поверхности:"+ str(S))


#Begin-7
print("Begin 7")
print ("""            ===============
             L=2*PI*R; S=PI*R*R
            =================""")
R=int(input("Введите радиус окружности:"))
PI=3.14
L=2*PI*R
S=PI*R*R
print("Длина окружности: "+str(L))

print("Площадь круга: "+str(S))

#Begin-8
print("Begin 8")
print ("""            ===============
             sredniy_arif=(a+b)/2
            =================""")
a=int(input("Введите число а: "))
b=int(input("Введите число b: "))
sredniy_arif=(a+b)/2
print("Средний арифметический значения двух число: "+str(sredniy_arif))


#Begin -8
print("Begin 8")
def arif_znach(a,b):
    return(a+b)/2
znach_p=arif_znach(6,8)
print(znach_p)

#Begin-9
print("Begin 9")
def chis_neot(a,b):
    return(a*b)**(1/2)
neot=chis_neot(3,4)
print(round(neot,2))

#begin-10
print("Begin 10")
def chi_l(a,b):
     raznost=a-b
     umnozheniya=a*b
     summa=a+b
     kvadr=a**2/b**2
     print("a-b= "+str(round(raznost,2))+ "  a*b="+str( round(umnozheniya,2))+"  a+b="+str(round(summa,2))+"  a**2/b**2="+str(round(kvadr,2)))
chi_l(3,5)


#begin-12
print("Begin 12")
def triangle_1(a,b):
    return (a**2+b**2)**0.5
test2=triangle_1(2,3)
def perimetr (a,b):
    return a+b+test2
test_2=perimetr(2,3)
print(round(test2,2))
 
#begin - 13
print("Begin 13")
def circle_1(R1,R2,PI=3.14):
    S1=PI*R1**2
    S2=PI*R2**2
    S=S2-S1
    print("S1="+str(round(S1,2))+ " S2="+str(round(S2,2))+ " S="+str(round(S,2)))
circle_1(4,6)

#begin-14
print("Begin 14")
def krug_1(R,PI=3.14):
    Length=2*PI*R
    Area=PI*R**2
    print("L="+str(round(Length,2))+"  S="+str(round(Area,2)))
krug_1(6)

#begin-15
print("Begin 15")
def diametr_1(D,PI=3.14):
    Length_1=PI*D
    Area_1=(PI*D**2)/4
    print("L="+str(round(Length_1,2))+" S="+str(round(Area_1,2)))
diametr_1(5)
print("""        ==================
         d=((x2-x1)^2+(y2-y1)^2)**(1/2)
         ===================""")
x1=int(input("Введите первый точка х1: "))
y1=int(input("Введите  первый точка у1: "))
x2=int(input("Введите второй точка х2: "))
y2=int(input(" Введите второй точки у2: "))
d= ((x2-x1)**2+(y2-y1)**2)**(1/2)
print (" Расстояние между двумя точками:  " +   str(d))\
#begin -18
print("Begin 16")
def otrezka_1(A,B,C):
    AC=C-A
    BC=B-C
    proizvedeniya=AC*BC
    print("AC*BC= "+str(proizvedeniya))
otrezka_1(2,3,2.5)
       

#begin-21
print("Begin 21")
def triangle_1(a,b,c):
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    print("P= "+str(p)+ "  S= "+str(round(area,2)))
triangle_1(2,3,4)
#begin-22
print("Begin 22")
def pereme_1(A,B):
    temp=A
    A=B
    B=temp
    
    print(A,B)
pereme_1(4,5)
#begin-23
print("Begin 23")
def perem_2(A,B,C):
    temp=A
    A=B
    B=C
    C=temp
    print(A,B,C)
perem_2(6,8,9)
#begin-24
print("Begin 24")
def perem_3(A,B,C):
    temp=A
    A=C
    C=B
    B=temp
    print(A,B,C)
perem_3(6,8,9)
#begin -25
print("Begin 25")
def func(x):
    y=3*x**6-6*x**2-7
    print("Y= "+str(y))
func(3)
#begin -26
print("Begin 26")
def func_1(x):
    y= 4*(x-3)**6-7*(x-3)**3+2
    print("Y= "+str(y))
func_1(3)
#begin-27
print("Begin 27")
def chislo(A):
    A2=A*A
    A4=A2*A2
    A8=A4*A4
    print("A2= "+str(A2)+" A4= "+str(A4)+" A8="+str(A8))
chislo(4)

#begin-28
print("Begin 28")
def chislo_1(A):
    A2=A*A
    A3=A2*A
    A5=A3*A2
    A10=A5*A5
    A15=A10*A5
    print("A2= "+str(A2)+" A3= "+str(A3)+" A5="+str(A5)+"  A10= "+str(A10)+ " A15="+str(A15))
chislo_1(4)
#begin-29
print("Begin 29")
def radian(x,PI=3.14):
    rad=(x*PI)/180
    print( "60 градус= "+str(round(rad,2) ))
radian(60)

#begin-30
print("Begin 30")
def radian_1(x,PI=180):
    radi=(x*180)/PI
    print( "60 радиан= "+str(round(radi,2))+"градус")
radian_1(60)

#begin-31
print("Begin 31")
def fare(Tf):
    Tc=(Tf-32)*5/9
    print(str(Tf)+" Фаренгейт равен "+str(round(Tc,2)))
fare(54)

#begin-32
print("Begin 32")
def fare_2(Tc):
    Tf=Tc*9/5+32
    print(str(Tc)+" целсий равен "+str(round(Tf,2)))
fare_2(54)
#begin-33
print("Begin 33")
def konfetka_2(A,X):
    konfet=A/X
    print("1кг="+str(konfet)+"рублей")
konfetka_2(3,24)

def konfetka_42(A,X,Y):
    konfet=(A*Y)/X
    print(str(Y)+"кг="+ str(konfet)+"рублей" )
konfetka_42(3,24,int(input("Введите значения сколько килограммов: ")))

#begin-34
print("Begin 34")
def choko_1(X,A,Y,B):
   choko=A/X
   iris=B/Y
   otnosheniya=choko/iris
   print("1кг шоколадь="+str(round(choko))+" 1кг ирис="+str(round(iris,2)))
   print("Во "+ str(round(otnosheniya,2))+" раз  шоколадь больше чем ирис")
choko_1(2,23,3,34)
 
#begin -35
print("Begin 35")
def lodka_1(V,U,T1,T2):
    S1=V*T1
    S2=(V-U)*T2
    S=S1+S2
    print( "Расстояния пройденный лодки: ",S)
lodka_1(4,2,4,2)
#Begin-36
print("Begin 36")
def auto_1(V1,V2,T,S):
    P=abs(S+(V1+V2)*T)
    print("Расстояния между ними через Т часов: "+str(P))
auto_1(4,7,3,20)

#Begin-37
print("Begin 37")
def auto(V1,V2,T,S):
    P=abs(S-(V1+V2)*T)
    print("Расстояния между ними через Т часов: "+str(P))
auto(4,7,3,20)

#Begin-40
print("Begin 40")

print("""       ========================
         A1*X+B1*Y=C1 Система линейных уравнений
         A2*X+B2*Y=C2
        =====================""")
A1=int(input(" Введите коэффициент А1: "))
B1=int(input(" Введите коэффициент В1: "))
C1=int(input(" Введите коэффициент С1: "))
A2=int(input(" Введите коэффициент А2: "))
B2=int(input(" Введите коэффициент В2: "))
C2=int(input(" Введите коэффициент С2: "))
D= A1*B2-A2*B1
X=(C1*B2-C2*B1)/D
Y=(A1*C2-A2*C1)/D

print(" Значение Х: "+ str(X))
print(" Значение У: "+ str(Y))

    
