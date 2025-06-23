import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Compute first term: π²/12
term1 = pi_squared / 12

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute second term: 2*(ln2)^2
term2 = 2 * (ln2 ** 2)

# Combine terms to get final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))