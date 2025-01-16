class Skolotajs:
    stunduSkaitsNedela = 0
    skolotajaTips = 0
    uzvards = "Nezinams"
    klase = "x.i"

class SakumskolasSkolotajs(Skolotajs):
    def __init__(self):
        self.skolotajaTips = 1
    def ievade(self):
        self.uzvards = input("Ievadiet uzvārdu --->")
    def izvade(self):
        print(f"Sākumskolas (tips -{self.skolotajaTips}")
class VidusskolasSkolotajs(Skolotajs):
    pirmaisPrieksmets = "x prieksmets"
    otraisPrieksmets = "y prieksmets"
    pirmaisPrieksmetsStundas = 0
    otraisPrieksmetsStundas = 0
    def cikStundasKopa(self):
        self.StunduSkaitsNedela = self.pirmaisPrieksmetsStundas + self.otraisPrieksmetsStundas
        return self.stunduSkaitsNedela
ss1 = SakumskolasSkolotajs()
ss1.izvade()
vs1 = VisusskolasSkolotajs()
vs1.izvade()