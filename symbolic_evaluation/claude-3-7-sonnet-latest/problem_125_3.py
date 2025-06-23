import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Numerator of the expression
numerator = mp.mpf(16)

# Denominator: 945 * π
denominator = mp.mpf(945) * mp.pi

# Compute the final result: 16 / (945 * π)
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))