import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate natural logarithm of 2
ln_2 = mp.log(2)

# Multiply by pi constant
pi_times_ln2 = mp.pi * ln_2

# Final result with 10 decimal precision
print(mp.nstr(pi_times_ln2, n=10))