#Program is to calculate the n=th power of a given number

#Given number
base = int(input("Enter the number: "))
#Power
exponent = int(input("Enter the power: "))

#Calculate power
result = base ** exponent

#Display result
print(f"{base} raised to the power {exponent} is: {result}")