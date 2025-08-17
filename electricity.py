units = int(input("Please enter Number of units you Consumed:"))

if units < 50:
    amount = units * 2.60
    surcharge = 25
elif units <= 100:
    amount = 130 + ((units - 50) * 5.26)
    surcharge = 35
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75
total = amount + surcharge
print("\nElectricity Bill = %.2f" % total)            