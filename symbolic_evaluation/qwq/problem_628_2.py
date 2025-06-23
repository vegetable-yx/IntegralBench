import mpmath as mp
mp.dps = 15

# Calculate the numerator: π + 2
numerator = mp.pi + 2

# Denominator is 8
denominator = 8

# Compute the final value by dividing and applying the negative sign
result = -numerator / denominator

print(mp.nstr(result, n=10))