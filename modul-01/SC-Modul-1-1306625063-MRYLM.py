print ("pemprograman konversi suhu")
print("Nama:M. Royan Y L M")
print("NIM: 1306625063")

print()
print("input suhu yang diinginkan")

x=float(input("suhu awal="))
y=float(input("suhu akhir="))
z=float(input("selang="))

print("TABEL KONVERSI")
print('=' * 65)
print("|{0:^5}{1:^15}{2:^15}{3:^15}".format("No","Celcius","Reamur","Fahreinheit"))
print('=' * 65)

n=1
while(x<=y):
    C = round(x,3)
    R = round (x*4/5, 3)
    F = round(x*9/5 + 32, 3)
    print("|{0:^5}{1:^15}{2:^15}{3:^15}|".format(n,C,R,F))
    n=n+1
    x=x+z

print('=' * 65)

print()
print("selesai")