# class MataKuliah
class MataKuliah:
    def __init__(self, kode, nama, sks) :
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def __str__(self):
        return f"- [{self.kode}] {self.nama} ({self.sks} SKS)"
    
    def __eq__(self, other):
        return self.kode == other

# class KRS
class KRS:
    def __init__(self, semester):
        self.semester = semester
        self._daftar_mk = []

    def tambah_mk(self, mk):
        for mata_kuliah in self._daftar_mk:
            if mata_kuliah.kode == mk.kode:
                raise ValueError("Mata kuliah sudah diambil")

        self._daftar_mk.append(mk)

    def total_sks(self):
        total = 0
        for mk in self._daftar_mk:
            total += mk.sks

        return total
            
    def __len__(self):
        return len(self._daftar_mk)
        
    def __str__(self):
        hasil = f"=== KRS Semester {self.semester} (Total: {self.total_sks()} SKS) ===\n"

        for mk in self._daftar_mk:
            hasil += str(mk) + "\n"

        return hasil

if __name__ == "__main__":

    mk1 = MataKuliah("CS1234", "Kalkulus 1", 3)
    mk2 = MataKuliah("CS456", "Matematika Diskrit 1",4)

    krs = KRS("2026/2027")
    krs.tambah_mk(mk1)
    krs.tambah_mk(mk2)

    print(krs)



