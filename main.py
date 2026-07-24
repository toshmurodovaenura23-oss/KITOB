class Kitob:
    def __init__(self, nomi):
        self.nomi = nomi
        self.oquvchilar = []

    def olish(self, oquvchi):
        self.oquvchilar.append(oquvchi)

    def qaytar(self, oquvchi):
        if oquvchi in self.oquvchilar:
            self.oquvchilar.remove(oquvchi)
            return f"{oquvchi} kitobni qaytardi."
        else:
            return "Bu kitob sizda emas."


kitob = Kitob("Python")

kitob.olish("Ali")
kitob.olish("Vali")

print(kitob.qaytar("Ali"))
print(kitob.qaytar("Hasan"))
print(kitob.oquvchilar)