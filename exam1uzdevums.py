class csddTransports():
    def ievade(self):
        self.zimols = "Audi"
        self.modelis = "A4"
        self.regNumurs = "22.10.2019"
        self.pilnaMasa = 1800
        self.degvVeids = "BG"
    def izvade(self):
        print(f"Automašīnas zīmols ir {self.zimols}, modelis {self.modelis}, reģistrācijas numurs {self.regNumurs}, pilna masa {self.pilnaMasa}, degvielas veids {self.degvVeids}")

t = csddTransports()
t.ievade()
t.izvade()