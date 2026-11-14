# Bikin class mobil
# parameter nya merk, harga.
# function nya cek Diskon
# Jika harga >= 500 jt maka diskon 10% jika kurang dari 500jt diskon nya 5%

class Mobil: 
    def __init__(self, merk,harga): 
        self.merk = merk
        self.harga = harga

    def cek_diskon(self):
        if self.harga >= 500000000:
            return self.harga * 0.10
        else:
            return self.harga * 0.05

mobil1 = Mobil ("Toyota",600000000)
mobil2 = Mobil ("Honda", 300000000)

diskon1 = mobil1.cek_diskon()
diskon2 = mobil2.cek_diskon()

print(f"Diskon {mobil1.merk}: Rp{diskon1}")
print(f"Diskon {mobil2.merk}: Rp{diskon2}")