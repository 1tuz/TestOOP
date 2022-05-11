

class Banks:
    def __init__(self, name, fact_adress, btype):
        self.name = name
        self.fact_adress = fact_adress
        self.btype = btype


rncb = Banks("RNCB", "Crimea", "commercial")
tinkof = Banks("Tinkoff", "Europe", "commercial")
sber = Banks("Sberbank", "Russia", "national")

print(rncb.name)
print(sber.fact_adress)
print(tinkof.name,tinkof.fact_adress,tinkof.btype)