import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm of 2
ln2_sq = ln2**2

# Compute first term: (ln2)^2 / 4
term1 = ln2_sq / 4

# Compute pi squared
pi_sq = mp.pi**2

# Compute second term: pi^2 / 24
term2 = pi_sq / 24

# Sum both terms
result = term1 + term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))