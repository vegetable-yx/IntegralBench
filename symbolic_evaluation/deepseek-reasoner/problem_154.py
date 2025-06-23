import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 32 to get final result
result = pi_cubed / 32

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))