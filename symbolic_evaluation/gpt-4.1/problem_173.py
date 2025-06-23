import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute numerator: 28815 * π
numerator = 28815 * mp.pi

# Denominator is 1769472
denominator = 1769472

# Final result is numerator divided by denominator
result = numerator / denominator

# Print result to 10 decimal places
print(mp.nstr(result, n=10))