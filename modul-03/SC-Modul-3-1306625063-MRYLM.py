import math
def mclaurin_sin (x,k):
    n = k - 1
    suku_sin = ((-1)**n)*(x**(2*n+1))/math.factorial(2*n + 1)
    return suku_sin

def mclaurin_cos (x,k):
    n = k - 1
    suku_cos = ((-1)**n)*(x**(2*n))/math.factorial(2*n)
    return suku_cos

def tabel():
    while True:
        print("Program Sinus Cosinus")
        print("Nama : M. Royan Y L M")
        print("NIM : 1306625063")
        print()
        besar_sudut = float(input("Besar Sudut (derajat) = "))
        sudut_rad = math.radians(besar_sudut)
        tv_sin = math.sin(sudut_rad)
        print(f"True Value Sin {besar_sudut:.1f} = {tv_sin:.3f}")
        tv_cos = math.cos(sudut_rad)
        print(f"True Value Cos {besar_sudut:.1f} = {tv_cos:.3f}")
        print()
        
        print("="*45)
        print(f"{'Suku ke':<5}|{'AV Sin':<7}|{'ER Sin (%)':<8}|{'AV cos':<10}|{'ER Cos (%)':<12}")
        print("="*45)
        suku_ke = 1
        av_sin = 0.0
        av_cos = 0.0 
        er_sin = 100.0
        er_cos = 100.0
        while er_sin >= 5.0 or er_cos >= 5.0:
            av_sin += mclaurin_sin(sudut_rad, suku_ke)
            av_cos += mclaurin_cos(sudut_rad, suku_ke)
            er_sin = abs((av_sin - tv_sin)/tv_sin)
            er_cos = abs((av_cos - tv_cos)/tv_cos)
            print(f"{suku_ke:<6}|{av_sin:8.2f}|{er_sin:9.2f}|{av_cos:10.2f}|{er_cos:9.2f}")
            suku_ke += 1
        print("="*45)
        print()
        
        ulang = input("Mau menghitung lagi (y/t)? = ")
        if ulang != "y":
            break
    
tabel()

print()
print("Selesai")