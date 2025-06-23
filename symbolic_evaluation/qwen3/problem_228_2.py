import mpmath as mp
mp.dps = 15

# Calculate pi^3
pi_cubed = mp.pi ** 3

# Divide by 48 to get final result
result = pi_cubed / 48

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))