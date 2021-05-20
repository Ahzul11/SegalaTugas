print("--- Kasir ---")
input("Nama Kasir : ")
int(input("No Struk   : "))
a = int(input("Jumlah barang yang akan dibeli : "))
ttl = []
i = 1
while i <= a:
    try:
        nama = input("Nama Barang " + str(i) + "    : ")
        satuan = int(input("Harga Satuan " + str(i) + "   : "))
        assert satuan > 0
        jumlah = int(input("Jumlah Barang " + str(i) + "  : "))
        assert jumlah > 0
        total = satuan * jumlah
        print("Total Harga " + str(i) + "    : " + str(total))
        ttl.append(total)
        i += 1
        print("\n")
    except AssertionError:
        print("Harus lebih dari 0")
    except ValueError:
        print("ValueError")


while True:
    try :
      totl = sum(ttl)
      print("Total bayar  : "+ str(totl))
      uang = int(input("Uang  : "))
      assert uang >= totl
      kemb = uang-totl
      print("Kembalian : "+str(kemb))
      break
    except AssertionError:
      print("Uang kurang bosku, gaboleh utang. Masukkan lagi")
    except ValueError:
      print("ValueError")
    
