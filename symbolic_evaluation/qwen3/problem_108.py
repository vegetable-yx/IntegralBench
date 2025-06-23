import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by 3
numerator_part = 3 * sqrt2

# Multiply by pi
product_with_pi = numerator_part * mp.pi

# Divide by 16 to get final result
result = product_with_pi / 16

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))