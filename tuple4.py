my_tuple = (1, 2, 3, 4)

# Using a loop
product = 1
for number in my_tuple:
    product *= number
print(f"Product using loop: {product}")

# Using reduce from functools
product_reduce = reduce(operator.mul, my_tuple)
print(f"Product using reduce: {product_reduce}")
# Output for both: Product: 24
