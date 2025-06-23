import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Compute numerator: 25 times pi squared
numerator = 25 * pi_sq

# Denominator is 1152
denominator = 1152

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))