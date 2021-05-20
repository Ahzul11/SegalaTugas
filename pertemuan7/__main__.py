#import sys
"""lists= ['a', 0,4]
for each in lists :
  try:
    print("Masukan ", each)
    r= 1/int(each)
    break
  except:
    print("Opsi!", sys.exc_info()[0],"terjadi.")
    print("Masukan Berikutnya.")
    print()
print("Kebalikan dari ", each, " = ", r)"""

"""try:
  x = int(input("Masukkan Angka : "))
  y = 1 /x
  print(y)
except ZeroDivisionError:
  print("kamu tidak dapat membagi dengan angka 0")
except ValueError:
  print("Masukkan data harus berupa bilangan integer")
except :
  print("Suatu kesalahan terjadi")
print("done")"""

"""orang = {"nama": "syuaib", "kota":"jepara", "umur": "20"}
e = input("masukkan atributnya : ")
try:
  print(orang[e])
except KeyError:
  print("terjadi error KeyError :",e)
finally:
  print("baris ini akan selesai dieksekusi")
print(orang)

print()

def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print("division by zero!")
  else :
    print("hasilnya adalah : ", result)
  finally:
    print("executing finally clause")
    print('')
divide(2, 1)
divide(2, 0)
divide("2", "1")"""

"""try :
  y = 1 / 0
except ZeroDivisionError:
  print("Oopsie....ZeroDivisionError")

try :
  y = 1 / 0
except ArithmeticError:
  print("Oopsie....ArithmeticError")

try :
  y = 1 / 0
except Exception:
  print("Oopsie....Exception")

try:
  y = 1 / 0
except BaseException:
  print("Oopsie....BaseException")

print()

try :
  print("5"/0)
except ArithmeticError:
  print("1...ArithmeticError")
except ZeroDivisionError:
  print("2...ZeroDivisionError")
except:
  print("3...")"""

"""def badFun(n):
  try:
    return 1/n
  except ArithmeticError:
    print("ArithmeticError, Aritmatika bermasalah")
  return None
badFun(0)
print("done\n")

def badFun(n):
  return 1 / n
try:
  badFun(0)
except ArithmeticError:
  print("Apa yang terjadi? Exception muncul!!")
print("selesai")"""

"""def badFun(n):
  1/n
  raise ZeroDivisionError

try:
  badFun(0)
except ArithmeticError:
  print("Apa yang terjadi ? error")
print("selesai.")

def badFun(n):
  try:
    return n/0
  except:
    print("aku melakukannya lagi! :(")
    raise
try: 
  badFun(0)
except ArithmeticError:
  print("Aku tahu !")
print("selesai")"""

"""from math import tan, radians
angle = int(input("Masukkan sudut integral dalam derajat: "))

#sudut harus !=90 +k*100
assert angle % 100 != 90
print(tan(radians(angle)))"""

"""the_list=[1,2,3,4,5]
ix = 0
do_it= True
while do_it :
  print(the_list[ix])
  ix +=1"""

"""print()
the_list = [12,3,4,5]
ix = 0
do_it = True
while do_it:
  try:
    print(the_list[ix])
    ix += 1
  except IndexError:
    do_it = False
print("Done")"""

