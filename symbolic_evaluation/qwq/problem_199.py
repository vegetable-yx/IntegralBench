import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate Struve H function of order 0 at 1
H0_1 = mp.struveh(0, 1)

# Combine components for final result
result = 2 * sqrt2 * H0_1

print(mp.nstr(result, n=10))