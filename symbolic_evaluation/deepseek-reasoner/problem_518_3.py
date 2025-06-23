import mpmath as mp
mp.dps = 15

# Direct assignment of the exact integer value
result = mp.mpf(4036)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))