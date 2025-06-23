import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute each term separately
constant_term = mp.mpf(2)
log_term = 4 * ln2
log_squared_term = 4 * (ln2 ** 2)
pi_squared_term = (mp.pi ** 2) / 12

# Combine all components
result = constant_term + log_term - log_squared_term - pi_squared_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))