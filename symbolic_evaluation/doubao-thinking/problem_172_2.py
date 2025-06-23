import mpmath as mp
mp.dps = 15

# Calculate simple fraction using exact values
numerator = mp.mpf(1)
denominator = mp.mpf(4)
result = numerator / denominator

print(mp.nstr(result, n=10))