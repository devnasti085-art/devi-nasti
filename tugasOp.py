#Operator
#Operator aritmatika
a = 5
b = 4
a = 9
c = 6
penjumlahan = a + b + c
sisabagi = a % c
perkalian = a * b * c
pembagian = c / b
pengurangan = a - b
perpangkatan = a ** b
pembagian_bulat = c // b
print(f"Hasil Penjumlahan {a} + {b} + {c} = {penjumlahan}")
print(f"sisa bagi {a} mod {c} = {sisabagi}")
print(f"hasil perkalian {a} * {b} * {c} = {perkalian}")
print(f"hasil perbagian {c} / {b} = {pembagian}")
print(f"hasil pengurangan {a} - {b} ={pengurangan}")
print(f"hasil perpangkatan {a} ** {b} ={perpangkatan}")
print(f"hasil pembagian_bulat {c} // {b} ={pembagian_bulat}")

#operator assigment

a += 2 #11 a = 9 + 2
a **= 2 #121 a = 11 ** 2
print(a)

#Operator perbandingan
perbandingan = a >= b #121 >= 2 true
print(perbandingan)

x = 6
y = 5
banding = x <= y #false

print(x != y)
print(banding)

#operator logika AND
print("----operator logika---")
opAnd = a >= b and x <=y and x != y
opOR = perbandingan or banding or x != y
opNOT = not opAnd
print(opAnd)
print(opOR)
print(opNOT)