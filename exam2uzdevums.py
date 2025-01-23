class Skolotajs:
    stunduSkaitsNedela = 0
    skolotajaTips = 0
    uzvards = "Nezinams"
    klase = "x.i"

class SakumskolasSkolotajs(Skolotajs):
    klase = "x.i"
    def __init__(self):
        self.skolotajaTips = 1
    def ievade(self):
        self.uzvards = input("Ievadiet sākumskolas skolotāja uzvārdu ---> ")
        self.klase =input("Ievadiet klasi ---> ")
        self.stunduSkaits = input("Ievadiet stundu skaitu ---> ")
    def izvade(self):
        print(f"Sākumskolas (tips -{self.skolotajaTips}")
class VidusskolasSkolotajs(Skolotajs):
    def __init__(self): 
        self.skolotajaTips = 3
    pirmaisPrieksmets = "x prieksmets"
    otraisPrieksmets = "y prieksmets"
    pirmaisPrieksmetsStundas = 0
    otraisPrieksmetsStundas = 0
    def cikStundasKopa(self):
        self.stunduSkaitsNedela = self.pirmaisPrieksmetsStundas + self.otraisPrieksmetsStundas
        return self.stunduSkaitsNedela
    def ievade(self):
        self.uzvards = input("Ievadiet vidusskolas skolotāja uzvārdu ---> ")
        self.pirmaisPrieksmets = input("Ievadiet pirmo priekšmetu ---> ")
        self.otraisPrieksmets = input("Ievadiet otro priekšmetu ---> ")
        self.pirmaisPrieksmetsStundas = int(input("Ievadiet pirmā priekšmeta kopstundu skaitu ---> "))
        self.otraisPrieksmetsStundas = int(input("Ievadiet otrā priekšmeta kopstundu skaitu ---> "))
    def izvade(self):
        print(f"Vidusskolas (tips -{self.skolotajaTips} skolotājs {self.uzvards} māca šādus priekšmetus ---> ")
        print(f"{self.pirmaisPrieksmets} un {self.otraisPrieksmets}, kopā {self.cikStundasKopa()} stundas.")
ss1 = SakumskolasSkolotajs()
ss1.ievade()
ss1.izvade()
vs1 = VidusskolasSkolotajs()
vs1.ievade()
vs1.izvade()