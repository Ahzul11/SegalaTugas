"""a = int(input("Apa aja input : "))
b = int(input("Apa aja input : "))

if b != 0 :
  print(a/b)
else :
  print('Gagal')
print("selesai")
"""
"""try :
  a = int(input("Apa aja input : "))
  b = int(input("Apa aja input : "))
  print(a/b)
except :
  print('Gagal')
print("selesai")"""

try:
  print("1")
  x = 1 / 0
  print("2")
except:
  print("Gagal")
print("3")