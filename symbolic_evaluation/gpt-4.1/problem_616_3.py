import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm of 2
ln2_sq = ln2 ** 2

# Compute pi squared
pi_sq = mp.pi ** 2

# Calculate first term: pi^2 / 48
term1 = pi_sq / 48

# Calculate second term: (ln2)^2 / 4
term2 = ln2_sq / 4

# Combine terms: result = term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))