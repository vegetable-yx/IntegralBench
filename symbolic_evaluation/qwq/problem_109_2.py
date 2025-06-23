import mpmath as mp
mp.dps = 15

# Directly use mpmath's pi constant
result = mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))