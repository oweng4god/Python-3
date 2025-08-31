#Program to convert decimal to binary

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

#Taking input from user
decimal_num = int(input("Enter adecimal number:  "))

#Conversation
binary_num = decimal_to_binary(decimal_num)

#Output
print("Binary number:", binary_num)