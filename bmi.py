berat = float(input("masukan berat dalam kg="))
tinggi = float(input("masukan tinggi dalam cm="))
tinggi = (tinggi/100)
print(tinggi)
tinggikuadrat = (tinggi*tinggi)
rumus = (berat/tinggikuadrat)
if (rumus > 30):
   print("obesitas") 
elif(rumus < 23 and rumus <= 29.9):
    print("berat badan berlebih")
elif(rumus > 18.5 and rumus <= 22.9):
    print("berat badan ideal")
else:
    print("berat badan kurang proposional")