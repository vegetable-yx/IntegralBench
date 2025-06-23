import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Compute -π²/6
term1 = -pi_sq / 6

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm to get ln²(2)
ln2_sq = ln2 ** 2

# Compute 2 * ln²(2)
term2 = 2 * ln2_sq

# Combine the terms: -π²/6 + 2 ln²(2)
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))