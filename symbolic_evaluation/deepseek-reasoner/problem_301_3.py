import mpmath as mp
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute first term: 4*ln2
term1 = 4 * ln2

# Compute second term: -4*(ln2)^2
term2 = -4 * (ln2 ** 2)

# Compute third term: -π²/12
term3 = -(mp.pi ** 2) / 12

# Combine all terms for final result
result = term1 + term2 + term3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))