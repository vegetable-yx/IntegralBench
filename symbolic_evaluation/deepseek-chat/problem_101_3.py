import mpmath as mp

# Set the decimal places for internal precision
mp.dps = 15

# Calculate the value of arcsin(1/4)
arcsin_val = mp.asin(1/4)

# Calculate the square root of 15
sqrt_15 = mp.sqrt(15)

# Multiply sqrt(15) by arcsin(1/4)
product = sqrt_15 * arcsin_val

# Subtract the product from 1
result = 1 - product

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))