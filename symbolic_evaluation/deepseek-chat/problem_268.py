import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate π²
pi_sq = mp.pi ** 2

# Calculate π⁴
pi_fourth = mp.pi ** 4

# Calculate ln(2)
ln2 = mp.log(2)

# Compute first term: (π²/8) * (ln(2))²
term1 = (pi_sq / 8) * (ln2 ** 2)

# Compute second term: 11π⁴/960
term2 = (11 * pi_fourth) / 960

# Combine terms: first term minus second term
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))