import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π squared
pi_sq = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate (ln2)^2 and multiply by 12
ln2_sq = ln2 ** 2
term2 = 12 * ln2_sq

# Combine terms in numerator and divide by denominator
numerator = pi_sq + term2
result = numerator / 48

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))