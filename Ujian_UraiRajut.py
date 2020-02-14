# Soal 1
class uraiRajutKata:
    def Urai(self, kata):
        self.kata = kata
        hasil = ''
        for s in range(len(kata)):
            hasil += kata[:s+1]
        return hasil
    def Rajut(self, kata):
        self.kata = kata
        hasil = ''
        i = -1
        for a in range(len(kata)):
            hasil += kata[i]
            i-=1
            if kata[i] == kata[i].capitalize():
                break
        return hasil

x = uraiRajutKata()
print(x.Urai('Code'))
print(x.Urai('Python'))
print(x.Urai('Purwadhika'))
print(x.Rajut('CCoCodCode'))