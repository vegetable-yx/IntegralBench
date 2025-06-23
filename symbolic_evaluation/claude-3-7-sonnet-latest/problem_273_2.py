import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2
# Compute pi^2 / 24
term1 = pi_sq / 24

# Calculate natural logarithm of 2
ln2 = mp.log(2)
# Compute (pi * ln(2)) / 8
term2 = (mp.pi * ln2) / 8

# Compute (ln(2))^2
ln2_sq = ln2 ** 2
# Compute (ln(2))^2 / 8
term3 = ln2_sq / 8

# Combine terms: π²/24 - (π ln2)/8 + (ln2)²/8
result = term1 - term2 + term3

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))