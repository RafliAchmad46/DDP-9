# nomor 1
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

# 
print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

# nomor 2
def is_genap(bil_genap):
    return bil_genap %2 == 0
# untuk memasukan  value
print(is_genap(4))
print(is_genap(7))    

# nomor 3
def nilai_lulus(nilai):
    if nilai >= 80:
        return 'lulus'
    else:
        return 'gagal'
# untuk mencetak value
print(nilai_lulus(80))
print(nilai_lulus(60))

# nomor 4
def bil_ganjil(angka):
    for i in range(1, angka, 2):
        print(i, end=" ")
# untuk memasukan value 
bil_ganjil(20)
    
        