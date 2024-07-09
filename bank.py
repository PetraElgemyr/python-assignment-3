"""
Skriv ett program som beräknar hur mycket pengar man får på ett bankkonto.
Om man sätter in 100 000kr (hundratusen kronor) och låter pengarna stå inne under 5 år.
När man kör programmet frågar det efter räntesatsen, som anges i procent t.ex. 3.5.
Som resultat visar programmet en tabell där man kan se hur mycket kapitalet har växt efter varje år. 

Felhantering behövs då användaren lätt kan ge felaktig input då räntor ofta anges 
med decimalpunkt och inte kommatecken. För att kunna omvandla textsträngen till ett flyttal 
måste vi hantera eventuella fel som kan uppstå.

För att slippa köra om programmet när man skrivit fel så använder vi en while-loop för att
fråga efter räntesatsen tills användaren skriver in en korrekt räntesats. Detta genom att använda 
None (motsvarande null i exempelvis typescript) väldigt kontrollerat. 

"""

def convertStringInputToFloat(inputString): 
    try:
        return float(inputString)
    except ValueError: 
        print("Felaktig räntesats angiven. Försök igen. Obs! Använd punkt som decimaltecken.")
        return None


bankAccount = 100000
yearlyInterest = None

while yearlyInterest is None: 
    inputString = input("Ange räntesatsen i procent, ex. 2.5: ")
    yearlyInterest = convertStringInputToFloat(inputString)


print("Utvecklingstabell för bankkonto")
print("===============================")
print("År\tSek")

for i in range(1, 6):
    bankAccount = bankAccount + (bankAccount * (yearlyInterest / 100))
    print("{}\t{}".format(i, int(bankAccount)))
