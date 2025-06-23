import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Calculate first term: (ln2)^2 divided by 4
term1 = (ln2 ** 2) / 4

# Calculate second term: pi^2 divided by 48
pi_squared = mp.pi ** 2
term2 = pi_squared / 48

# Combine both terms for final result
result = term1 + term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))