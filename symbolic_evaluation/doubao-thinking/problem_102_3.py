import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π²
pi_squared = mp.pi ** 2

# Compute first term: π²/24
term1 = pi_squared / 24

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute (ln2)^2
ln2_squared = ln2 ** 2

# Calculate second term: (ln2)^2 / 2
term2 = ln2_squared / 2

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))