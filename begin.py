
#Begin -8
def arif_znach(a,b):
    return(a+b)/2
znach_p=arif_znach(6,8)
print(znach_p)

#Begin-9
def chis_neot(a,b):
    return(a*b)**(1/2)
neot=chis_neot(3,4)
print(round(neot,2))

#begin-10
def chi_l(a,b):
     raznost=a-b
     umnozheniya=a*b
     summa=a+b
     kvadr=a**2/b**2
     print("a-b= "+str(round(raznost,2))+ "  a*b="+str( round(umnozheniya,2))+"  a+b="+str(round(summa,2))+"  a**2/b**2="+str(round(kvadr,2)))
chi_l(3,5)


#begin-12
def triangle_1(a,b):
    return (a**2+b**2)**0.5
test2=triangle_1(2,3)
def perimetr (a,b):
    return a+b+test2
test_2=perimetr(2,3)
print(round(test2,2))
 
#begin - 13
def circle_1(R1,R2,PI=3.14):
    S1=PI*R1**2
    S2=PI*R2**2
    S=S2-S1
    print("S1="+str(round(S1,2))+ " S2="+str(round(S2,2))+ " S="+str(round(S,2)))
circle_1(4,6)

#begin-14
def krug_1(R,PI=3.14):
    Length=2*PI*R
    Area=PI*R**2
    print("L="+str(round(Length,2))+"  S="+str(round(Area,2)))
krug_1(6)

#begin-15
def diametr_1(D,PI=3.14):
    Length_1=PI*D
    Area_1=(PI*D**2)/4
    print("L="+str(round(Length_1,2))+" S="+str(round(Area_1,2)))
diametr_1(5)
 
#begin -18
def otrezka_1(A,B,C):
    AC=C-A
    BC=B-C
    proizvedeniya=AC*BC
    print("AC*BC= "+str(proizvedeniya))
otrezka_1(2,3,2.5)
 
#begin-33
def konfetka_2(A,X):
    konfet=A/X
    print("1кг="+str(konfet)+"рублей")
konfetka_2(3,24)

def konfetka_42(A,X,Y):
    konfet=(A*Y)/X
    print(str(Y)+"кг="+ str(konfet)+"рублей" )
konfetka_42(3,24,int(input("Введите значения сколько килограммов: ")))

#begin-34
def choko_1(X,A,Y,B):
   choko=A/X
   iris=B/Y
   otnosheniya=choko/iris
   print("1кг шоколадь="+str(round(choko))+" 1кг ирис="+str(round(iris,2)))
   print("Во "+ str(round(otnosheniya,2))+" раз  шоколадь больше чем ирис")
choko_1(2,23,3,34)
 
#begin -35
def lodka_1(V,U,T1,T2):
    S1=V*T1
    S2=(V-U)*T2
    S=S1+S2
    print( "Расстояния пройденный лодки: ",S)
lodka_1(4,2,4,2)
#Begin-36
def auto_1(V1,V2,T,S):
    P=abs(S+(V1+V2)*T)
    print("Расстояния между ними через Т часов: "+str(P))
auto_1(4,7,3,20)

#Begin-37
def auto(V1,V2,T,S):
    P=abs(S-(V1+V2)*T)
    print("Расстояния между ними через Т часов: "+str(P))
auto(4,7,3,20)
