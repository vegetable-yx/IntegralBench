import mpmath as mp
mp.dps = 15

# Calculate pi constant using mpmath
pi_value = mp.pi

# Compute pi divided by 2
result = pi_value / 2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))