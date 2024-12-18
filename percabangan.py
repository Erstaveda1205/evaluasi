# mengkategorikan layak tidaknya seseorang dalam menonton film
# indikatornya adalah usia
# jika usianya lebih dari 17 tahun maka layak
# jika tidak maka belum layak 

usia = int(input("masukkan usia anda ="))

if( usia > 17 ):
    print("layak menonton film")

# kategorikan kelulusan dari nilai
# indikatornya adalah nilai
# syarat:
# lulus jika nilai > 90
# tidak lulus jika nilai < 90
nilai = int(input("masukkan nilai anda ="))

if( nilai > 90 ):
    print("selamat anda lulus")
else :
    print("maaf anda gagal / tidak lulus")