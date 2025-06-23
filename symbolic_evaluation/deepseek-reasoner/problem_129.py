import mpmath as mp
mp.dps = 15

# Directly use mpmath's constant for pi
result = mp.pi

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))