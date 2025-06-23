import mpmath as mp

mp.dps = 15  # Set internal precision for calculations

# Calculate components of the analytical solution
pi_term = mp.pi
constant_term = mp.mpf(2)

# Compute the final result using the analytical expression π - 2
result = pi_term - constant_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))