import mpmath as mp
mp.dps = 15

# Assign the exact integer value using mpmath's multiprecision float
result = mp.mpf(3)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))