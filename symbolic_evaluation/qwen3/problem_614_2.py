import mpmath as mp
mp.dps = 15

# Calculate the simple fraction using exact precision
numerator = mp.mpf(1)
denominator = mp.mpf(2)
result = numerator / denominator

print(mp.nstr(result, n=10))