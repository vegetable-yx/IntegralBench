import mpmath as mp
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Divide by 12 to get the final result
result = pi_squared / 12

print(mp.nstr(result, n=10))