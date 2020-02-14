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
        for a in range(len(kata)):
            hasil += kata[-1:]
            i -=1 
        return hasil

x = uraiRajutKata()
print(x.Urai('Code'))
print(x.Urai('Python'))
print(x.Urai('Purwadhika'))
print(x.Rajut('CCoCodCode'))