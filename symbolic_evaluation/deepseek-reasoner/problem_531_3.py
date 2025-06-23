import mpmath as mp
mp.dps = 15

# Calculate simple fraction using exact rational numbers
numerator = mp.mpf(5)
denominator = mp.mpf(6)
result = numerator / denominator

print(mp.nstr(result, n=10))