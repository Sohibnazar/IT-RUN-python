#Begin-40

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
