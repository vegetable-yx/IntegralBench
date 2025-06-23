import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the numerator: π * √2
numerator = mp.pi * mp.sqrt(2)

# Divide the numerator by 4 to get the final result
result = numerator / 4

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))