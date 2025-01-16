from abc import ABC, abstractmethod
class Dzivnieks(ABC):
    def __init__(self, vards, kajas):
        self.vards = vards
        self.kajas = kajas
    @abstractmethod
    def skanja(self):
        print("random animal noise")
    def __str__(self):
        return f"{self.vards} un {self.kajas} kajas"
        
class Suns(Dzivnieks):
    def __init__(self, vards, kajas):
        super().__init__(vards, kajas)
        self.vards = "Komisars " + self.vards
    def skanja(self):
        print("Vau! Vau! Gaf! Gaf!")

class Kakjis(Dzivnieks):
    def __init__(self, vards, kajas):
        super().__init__(vards, kajas)
        self.vards = "Minkans " + self.vards
    def skanja(self):
        print("Mur Mjau!")

class Govs(Dzivnieks):
    def skanja(self):
        print("MUUUUUUUU!")

d1 = Govs("Gauja", 4)
d1.skanja()
print(d1)
d1.skanja()

s1 = Suns("Reksis", 4)
print(s1)
s1.skanja()

k1 = Kakjis("Murcis", 4)
print(k1)
k1.skanja()
dzivniekuSaraksts = []
dzivniekuSaraksts.append(Suns("Reksis", 3))
dzivniekuSaraksts.append(Suns("Volvis", 4))
dzivniekuSaraksts.append(Suns("Caps", 4))
dzivniekuSaraksts.append(Suns("Kakjis", 3))
dzivniekuSaraksts.append(Kakjis("Murcis", 4))
dzivniekuSaraksts.append(Kakjis("Burkaans", 4))
dzivniekuSaraksts.append(Govs("Gauja", 4))

print("###########################################################")
for dzivnieks in dzivniekuSaraksts:
    print(dzivnieks)
    dzivnieks.skanja()