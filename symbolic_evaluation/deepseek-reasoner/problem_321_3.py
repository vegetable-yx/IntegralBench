import mpmath as mp
mp.dps = 15

# Assign the exact integer value using mpmath type
result = mp.mpf(2)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))