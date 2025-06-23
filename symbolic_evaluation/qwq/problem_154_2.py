import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Compute π²/4 term
term1 = pi_squared / 4

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute 2*(ln2)^2 term
term2 = 2 * (ln2 ** 2)

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))