print("Program Mencari Faktor Bilangan")
print("Nama : M. Royan Y L M")
print("NIM : 1306625063")
print()
while True:
    print()
    n1 = int(input("masukan sembarang bilangan < 100 (masukan 0 untuk selesai): "))
    print()
    if n1 == 0:
        print("selesai")
        break

    if n1 >= 100:
        print("error")
        break 

    f1 = []
    for i in range(1,n1+1):
        if n1%i == 0:
            f1.append(i)
    print()
    print(f"bilangan {n1} -> faktornya = {f1}")

