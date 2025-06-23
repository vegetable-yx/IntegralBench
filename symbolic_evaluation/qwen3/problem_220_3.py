import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by coefficient 5
numerator = 5 * sqrt2

# Multiply by pi
numerator_pi = numerator * mp.pi

# Divide by 8 to get final result
result = numerator_pi / 8

print(mp.nstr(result, n=10))