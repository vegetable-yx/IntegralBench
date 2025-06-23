import mpmath as mp
mp.dps = 15

# Assign the exact integer value using mpmath's arbitrary precision
result = mp.mpf(626)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))