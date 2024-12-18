# soal ke 20

def check_equation(x, y, z):
    return x**2 + y**2 == z**2

#contoh pasangan nilai (x, y, z)
pairs = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]

for x, y, z in pairs:
    is_true = check_equation(x, y, z)
    if is_true:
        result = "kebenaran"
    else:
        result = "kesalahan"
    print("untuk x={}, y={}, z={} : persamaan benar? {}".format(x, y, z, result))

# soal ke 2

def solve_linear_equation(a, b):
    if a == 0:
        return None # persamaan tidak memiliki solusi jika a = 0
    x = -b / a
    return x

# input koefisien-koefisien persamaan linear
a = float(input("masukkan koefisien a= "))
b = float(input("masukkan koefisien b= "))

# menyelesaikan persamaan 
solution = solve_linear_equation(a, b)

# mencetak solusi
if solution is None:
    print("persamaan tidak memiliki solusi.")

else: 
    print("solusi persamaan liner:")
    print("x =", solution)

# soal ke 3

def seri(r1,r2,r3,r4):
    Rtotal = r1+ r2+ r3+ r4
    print(Rtotal)

def parallel(r1, r2):
    Rtotal = r1 * r2 / r1 * r2
    print(Rtotal)

print("1.seri")
print("2.paralell")

pilihan = int(input("masukkan pilihan anda 1, 2 = "))
if pilihan == 1:
    r1 = int(input("masukkan r1 seri ="))
    r2 = int(input("masukkan r2 seri ="))
    r3 = int(input("masukkan r3 seri ="))
    r4 = int(input("masukkan r4 seri ="))
    seri(r1, r2, r3, r4)

elif pilihan == 2:
    r1 = int(input("masukkan r1 parallel ="))
    r2 = int(input("masukkan r2 parallel ="))
    parallel (r1,r2)

else:
    print("maaf pilihan anda tidak ada")

# soal ke 9

print("mencari energi potensi dan energi mekanik")
def energi_potensial(m , g , h):
    hasil = m * g * h
    print(hasil)
m = int(input("masukan nilai = "))
g = int(input("masukan nilai = "))
h = int(input("masukan nilai = "))
energi_potensial(m , g , h)

def energi_mekanik(ep , ek):
    hasil = ep + ek
    print(hasil)
ep = int(input("masukan nilai = "))
ek = int(input("masukan nilai = "))
energi_mekanik(ep,ek)

# soal ke 19

def cek_relasi(himpunan_a, himpunan_b):
    for elemen_a in himpunan_b:
        if elemen_a == elemen_a:
            return True 

def cari_bilangan_ganjil(himpunan):
    bilangan_ganjil = [bilangan for bilangan in himpunan if bilangan % 2 != 0]
    return bilangan_ganjil

himpunan_a = [1, 2, 3, 4, 5]
himpunan_b = [4, 5, 6, 7, 8]
himpunan_c = [2, 4, 6, 8, 10]
himpunan_d = [1, 3, 5, 7, 9]

if cek_relasi(himpunan_a, himpunan_b):
    print("himpunan A memiliki relasi dengan himpunan B")
else:
    print("himpunan A tidak memiliki relasi dengan himpunan B")

bilangan_ganjil_c = cari_bilangan_ganjil(himpunan_c)
print("bilangan ganjil dari himpunan c:", bilangan_ganjil_c)

bilangan_ganjil_d = cari_bilangan_ganjil(himpunan_d)
print("bilangan ganjil dari himpunan D:", bilangan_ganjil_d)

# soal ke 8

print("mencari tekanan dan gaya tampung")
def tekanan(p , q , h):
    hasil = p * q * h
    print(hasil)
p = int(input("masukkan nilai = "))
q = int(input("masukkan nilai = "))
h = int(input("masukkan nilai = "))
tekanan(p , q , h)

def gaya_tampung(p , v , q):
    hasil = p * v * q
    print(hasil)
p = int(input("masukkan nilai = "))
v = int(input("masukkan nilai = "))
q = int(input("masukkan nilai = "))
tekanan(p , v , q)

# soal ke 17

def c(a, b):
    c = (a**2 + b**2)
    print("hasil perhitungan adalah", c)
a = float(input("masukkan nilai a = "))
b = float(input("masukkan nilai b = "))

c(a, b)