import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by coefficient 3
three_sqrt2 = 3 * sqrt2

# Multiply by pi
product = three_sqrt2 * mp.pi

# Apply negative sign
result = -product

print(mp.nstr(result, n=10))