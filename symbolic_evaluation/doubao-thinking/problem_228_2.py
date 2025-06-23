import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate first term: π²/12
term1 = pi_squared / 12

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate (ln2)^2
ln2_squared = ln2 ** 2

# Calculate second term: (ln2)^2 / 2
term2 = ln2_squared / 2

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))