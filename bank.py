"""
Skriv ett program som beräknar hur mycket pengar man får på ett bankkonto.
Om man sätter in 100 000kr (hundratusen kronor) och låter pengarna stå inne under 5 år.
När man kör programmet frågar det efter räntesatsen, som anges i procent t.ex. 3.5.
Som resultat visar programmet en tabell där man kan se hur mycket kapitalet har växt efter varje år. 
"""

bankAccount = 100000
yearlyInterest =float(input("Ange räntesatsen i procent, ex. 2.5: "))
print("Utvecklingstabell för bankkonto")
print("===============================")
print("År\tSek")

for i in range(1, 6):
    bankAccount = bankAccount + (bankAccount * (yearlyInterest / 100))
    print("{}\t{}".format(i, int(bankAccount)))
