
#integer-1
print("integer 1")
def metr(L):
    metr_1=L/100
    print( str(L)+"  сантиметр равен "+ str(metr_1)+" метр")
metr(int(input("Введите расстояние: ")))

#integer-2
print("integer 2")
def killo(M):
    killo_1=M/1000
    print( str(M)+"  киллограмм "+ str(killo_1)+" тонна.")
killo(int(input("Введите масса: ")))
#integer-3
print("integer 3")
def byte(B):
    byte_1=B/1024
    print( str(B)+"  байтов равен  "+ str(round(byte_1,2))+" киллобайтов")
byte(int(input("Введите размер файла в байтах: ")))
#integer -4
print("integer 4")
def otrez(A,B):
    length=A//B
    print("Количество отрезков "+str(B)+" размещенных на отрезке "+str(A)+" равен "+str(length))
otrez(int(input("Длина ортезка А:")),int(input("Длина отрезка В: ")) )
#integer -5
print("integer 5")
def otrez_1(A,B):
    length_1=A%B
    print(  "Длину незанятой отрезки "+str(A)+" равен "+str(length_1))
otrez_1(int(input("Длина ортезка А:")),int(input("Длина отрезка В: ")) )
#integer -6
print("integer 6")
def dvuznach_1(A):
     
    chislo_des=A//10
    chislo_ed=A%10
    print("Его левая часть равен: "+str(chislo_des) +"  Его правая часть равен: "+  str( chislo_ed))
dvuznach_1(int(input("Введите двузначное число: " )))
#integer -7
print("integer 7")
def chislo_1(A):
    chislo_sum=(A//10)+(A%10)
    chislo_proiz=(A//10)*(A%10)
    print("Сумма этих чисел равен : "+str(chislo_sum) +" Произведения этих чисел равен:  "+  str( chislo_proiz))
chislo_1(int(input("Введите двузначное число: " )))

#integer -8
print("integer 8")
def trekh_1(A):
     chislo_trekh=A//100
     print("Его пeрвая число равен: " +  str( chislo_trekh))
trekh_1(int(input("Введите трехзначное число: " )))


#integer -9
print("integer 9")
def dvuznach_2(A):
     
    chislo_des=A//10
    chislo_ed=A%10
    print("Число равен: "+str(chislo_ed) +  str( chislo_des))
dvuznach_2(int(input("Введите двузначное число: " )))
#integer -10
print("integer 10")
def trekh_1(A):
     chislo_1=(A%10)*10+((A%100)//10)
     print("Первая число равен: "+str(chislo_1) )
trekh_1(int(input("Введите трехзначное  число: " )))

#integer -11
print("integer 11")
def trekh_2(A):
     chislo_sum=(A%10)+((A%100)//10)+(A//100)
     chislo_proiz=(A%10)*((A%100)//10)*(A//100)
     print("Сумма этих чисел равен : "+str(chislo_sum) +" Произведения этих чисел равен:  "+  str( chislo_proiz))
trekh_2(int(input("Введите трехзначное  число: " )))
#integer -12
print("integer 12")
def trekh_3(A):
     chislo_3=(A%10)*100+((A%100)//10*10)+(A//100)
     print(" Число наоборот: "+str(chislo_3))
trekh_3(int(input("Введите трехзначное  число: " )))

#integer -13
print("integer 13")
def trekh_4(A):
     chislo_4=(A%10)+(((A%100)//10)*100)+(A//100)*10
     print(" После перестановки: " +str(chislo_4))
trekh_4(int(input("Введите трехзначное  число: " )))

#integer -14
print("integer 14")
def trekh_5(A):
     chislo_5=(A%10)*100+A//10
     print(" После перестановки: " +str(chislo_5))
trekh_5(int(input("Введите трехзначное  число: " )))
#integer -15
print("integer 15")
def trekh_6(A):
     chislo_6=((A%100)//10)*100+(A//100)*10+(A%10)
     print(" После перестановки: " +str(chislo_6))
trekh_6(int(input("Введите трехзначное  число: " )))

#integer -16
print("integer 16")
def trekh_6(A):
     chislo_6=(A//100)*100+(A%100)//10+((A%10)*10)
     print(" После перестановки: " +str(chislo_6))
trekh_6(int(input("Введите трехзначное  число: " )))
#integer -17
print("integer 17")
def trekh_6(A):
     chislo_6=(A%1000)//100
     print(" Число соответствующая разряду сотен в записи этого числа: " +str(chislo_6))
trekh_6(int(input("Введите трехзначное  число: " )))
#integer -18
print("integer 18")
def trekh_6(A):
     chislo_6=(A%10000)//1000
     print(" Число соответствующая разряду тысячу в записи этого числа: " +str(chislo_6))
trekh_6(int(input("Введите четырехзначное  число: " )))


#integer-19
print("integer 19")
def minut_1(N):
    minut=N//60
    print("Количество  минут: "+ str(minut))
minut_1(651)



#integer-20
print("integer 20")
def sec_1(N):
    sec=N//3600
    print("Количество часов: "+ str(sec))
sec_1(3651)

#integer-21
print("integer 21")
def minut_2(N):
    mint=N%3600
    print("Количество минут  с последней минуты: "+ str(mint))
minut_2(30651)
#integer-22
print("integer 22")
def sec_2(N):
    sec1=N%60
    print("Количество секунд  с последного часа: "+ str(sec1))
sec_2(351)

#integer-23
print("integer 23")
def minut_3(N):
    mint1=(N%60)%3600
    print("Количество минут  с последней часа: "+ str(mint1))
minut_3(34651)




#integer - 24
print(" integer 24")
def nedeli_1(K):
    D= K%7
    print("Номер дня недели: "+str(D))
"""
    " Восскресения-01"
    " Понедельник-02"
    " Вторник -03"
    " Среда-04"
    " Четверг-05"
    " Пятница-06"
    " Суббота-07"
"""
nedeli_1(124)


#integer - 25
print(" integer 25")
def nedeli_2(K):
    D= (K+3)%7
    print("Номер дня недели: "+str(D))
"""
    " Восскресения-01"
    " Понедельник-02"
    " Вторник -03"
    " Среда-04"
    " Четверг-05"
    " Пятница-06"
    " Суббота-07"
"""
nedeli_2(324)
#integer - 26
print(" integer 26")
def nedeli_3(K):
    D= ((K+4)%7)+1
    print("Номер дня недели: "+str(D))
"""
    " Восскресения-01"
    " Понедельник-02"
    " Вторник -03"
    " Среда-04"
    " Четверг-05"
    " Пятница-06"
    " Суббота-07"
"""
nedeli_3(334)

#integer - 27
print(" integer 27")
def nedeli_3(K):
    D= ((K+4)%7)+1
    print("Номер дня недели: "+str(D))
"""
    " Восскресения-01"
    " Понедельник-02"
    " Вторник -03"
    " Среда-04"
    " Четверг-05"
    " Пятница-06"
    " Суббота-07"
"""
nedeli_3(334)

#integer - 28
print(" integer 28")
def nedeli_3(K,N):
    D= ((K+N-2)%7)+1
    print("Номер дня недели: "+str(D))
"""
    " Восскресения-01"
    " Понедельник-02"
    " Вторник -03"
    " Среда-04"
    " Четверг-05"
    " Пятница-06"
    " Суббота-07"
"""
nedeli_3(334,7)


         
#integer - 29
print(" integer 29")
def kvad(A,B,C):
    nalo=(A*B)//C**2
    print(nalo)
kvad(12,7,2)
#integer - 30
print(" integer 30")
def era(N):
    let=N//100
    if let==0:
       
        print( int(let))
    else:
        print (int(let)+1)
era(1100)


    

        
    










