def sommatrice(lista):
    ris=0
    for elem in lista:
        ris+=elem
    print("La somma di tutti gli elementi della lista è "+str(ris))


num=int(input("Dimensione lista: "))
arr=list()

for i in range(num):
    ele=int(input("Inserire elemento "+(str(i+1))+": "))
    arr.append(ele)
print(arr)
sommatrice(arr)