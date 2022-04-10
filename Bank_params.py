class Banks:
    def __init__(self, name, adress, btype):
        self.name = name
        self.adress = adress
        self.btype = btype


rncb = Banks("RNCB", "Crimea", "commercial")
tinkof = Banks("Tinkoff", "Europe", "commercial")
sber = Banks("Sberbank", "Russia", "national")

print(rncb.name)
print(sber.adress)
print(tinkof.name,tinkof.adress,tinkof.btype)