import mpmath as mp
mp.dps = 15

# Calculate pi constant
pi = mp.pi

# Compute pi divided by 2
half_pi = pi / 2

# Apply negative sign to get final result
result = -half_pi

print(mp.nstr(result, n=10))