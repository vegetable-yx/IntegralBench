import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by 5
five_sqrt2 = 5 * sqrt2

# Multiply by pi
numerator = five_sqrt2 * mp.pi

# Divide by 8 to get final result
result = numerator / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))