class csddTransports():
    def ievade(self):
        self.zimols = "Audi"
        self.modelis = "A4"
        self.regNumurs = "22.10.2019"
        self.pilnaMasa = 1800
        self.degvVeids = "BG"
    def izvade(self):
        print(f"Zīmols: {self.zimols} \nmodelis: {self.modelis} \nreģistrācijas numurs: {self.regNumurs} \npilna masa: {self.pilnaMasa} kg \ndegvielas veids:{self.degvVeids}")

t = csddTransports()
t.ievade()
t.izvade()