import math
class kubs:
    def ievade(self):
        self.malasGarums = int(input("Ievadiet malas garumu, cm: "))
        self.krasasNosaukums = input("Ievadiet kuba krāsu: ")
    def izvade(self):
        self.kubaTilpums = pow(self.malasGarums, 3)
        print(f"Kuba krāsa ir {self.krasasNosaukums}, kuba tilpums ir {self.kubaTilpums} cm3")
    def kubg(self):
        self.krasasNosaukums = "zaļa"
        self.malasGarums = 10
        print(f"Kubg krāsa {self.krasasNosaukums}, malas garums {self.malasGarums} cm")
    def kubr(self):
        self.krasasNosaukums = "sarkana"
        self.malasGarums = 1
        print(print(f"Kubr krāsa {self.krasasNosaukums}, malas garums {self.malasGarums} cm"))
    

k = kubs()
k.ievade()
k.izvade()