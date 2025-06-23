import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square roots separately
sqrt_11 = mp.sqrt(11)  # sqrt(11)
sqrt_6 = mp.sqrt(6)    # sqrt(6)

# Compute terms in the numerator
term1 = 56 * sqrt_11   # 56 * sqrt(11)
term2 = 4 * sqrt_6     # 4 * sqrt(6)

# Combine numerator terms
numerator = term1 - term2  # 56*sqrt(11) - 4*sqrt(6)

# Divide by denominator to get final result
result = numerator / 12    # (56*sqrt(11) - 4*sqrt(6)) / 12

# Print result to 10 decimal places
print(mp.nstr(result, n=10))