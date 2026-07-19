class Kitob:
    def __init__(self, nomi, muallifi, yili):
        self.nomi = nomi
        self.muallifi = muallifi
        self.yili = yili
        self.oquvchilar = []

kitob1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 1926)
kitob2 = Kitob("Mehrobdan chayon", "Abdulla Qodiriy", 1929)

print(kitob1.oquvchilar)
print(kitob2.oquvchilar)
