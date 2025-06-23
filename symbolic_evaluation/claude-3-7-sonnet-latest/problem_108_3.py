import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate square root of 2
sqrt_val = mp.sqrt(2)

# Multiply by pi: π * √2
pi_sqrt_product = mp.pi * sqrt_val

# Multiply by 8: 8 * π * √2
numerator = 8 * pi_sqrt_product

# Divide by 9 to get final result
result = numerator / 9

# Print result with 10 decimal places
print(mp.nstr(result, n=10))