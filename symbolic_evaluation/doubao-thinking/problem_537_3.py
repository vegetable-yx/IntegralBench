import mpmath as mp
mp.dps = 15

# Assign the exact integer value with mpmath precision
result = mp.mpf(3)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))