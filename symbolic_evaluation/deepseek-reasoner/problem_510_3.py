import mpmath as mp
mp.dps = 15

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute the numerator: 7 * sqrt(3) * pi
numerator = 7 * sqrt3 * mp.pi

# Divide by 9 to get the final result
result = numerator / 9

print(mp.nstr(result, n=10))