start = int(input("Enter the start of range: "))
end = int(input("Enter the end the end of range:"))

squares = []
even_squares = []
odd_squares = []

for n in range(start, end + 1):
    square = n ** 2
    squares.append(square)
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("All squares:", squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)        