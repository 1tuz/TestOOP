from Bank_params import Banks

rncb = Banks("RNCB", "Crimea", "commercial")
tinkof = Banks("Tinkoff", "Europe", "commercial")
sber = Banks("Sberbank", "Russia", "national")

print(rncb.name, rncb.adress)