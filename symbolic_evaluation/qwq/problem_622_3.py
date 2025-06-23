import mpmath as mp
mp.dps = 15

# Calculate the numerator (π - 2)
numerator = mp.pi - 2

# Divide by 4 to get final result
result = numerator / 4

print(mp.nstr(result, n=10))