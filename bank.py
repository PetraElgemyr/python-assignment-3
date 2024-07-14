"""
Uppgift
Skriv ett program som beräknar hur mycket pengar man får på ett bankkonto.
Om man sätter in 100 000kr (hundratusen kronor) och låter pengarna stå inne under 5 år.
När man kör programmet frågar det efter räntesatsen, som anges i procent t.ex. 3.5.
Som resultat visar programmet en tabell där man kan se hur mycket kapitalet har växt efter varje år.

Planering
input -> validering för float -> beräkning -> output i tabellform

Användare ska kunna ange räntesatsen i procent genom en input.
Programmet ska sen kolla om användaren skrivit in en korrekt räntesats och kan omvandlas från string till float.
Om användaren skrivit in en felaktig räntesats ska programmet be användaren att skriva in en ny räntesats.
Om det är en korrekt räntesats ska programmet beräkna och skriva ut en tabell som visar hur mycket pengarna 
har växt efter varje år.


För att slippa köra om programmet när man skrivit fel så använder vi en while-loop för att
fråga efter räntesatsen tills användaren skriver in en korrekt räntesats. Detta genom att använda
None (motsvarande null i exempelvis typescript) väldigt kontrollerat. Kan även använda en boolean
i funktionen så att true/false returneras. Då använder man true eller false i while-loopens villkor.
Sedan tilldela inputen till räntevariabeln beroende på true/false. (Detta för att slippa pilla med none)
"""


def convertStringInputToFloat(inputString):
    try:
        return float(inputString)
    except ValueError:
        print(
            "Felaktig räntesats angiven. Försök igen. Obs! Använd punkt som decimaltecken."
        )
        return None


bankAccount = 100000.00
yearlyInterest = None

while yearlyInterest is None:
    inputString = input("Ange räntesatsen i procent, ex. 2.5: ")
    yearlyInterest = convertStringInputToFloat(inputString)


print("Utvecklingstabell för bankkonto")
print("===============================")
print("År\tSek")

for i in range(1, 6):
    bankAccount = bankAccount + (bankAccount * (yearlyInterest / 100.00))
    print("{}\t{:.2f}".format(i, bankAccount))
