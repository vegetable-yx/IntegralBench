import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π²
pi_squared = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute the term (ln2 - 1/2)
ln2_minus_half = ln2 - mp.mpf(1)/2

# Combine all components to get the final result
result = (pi_squared * ln2_minus_half) / 8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))