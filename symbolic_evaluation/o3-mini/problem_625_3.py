import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply pi by the square root of 2
pi_sqrt2 = mp.pi * sqrt2

# Divide the product by 4 to get the final result
result = pi_sqrt2 / 4

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))