import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate denominator
denominator = 2019

# Compute pi divided by denominator
pi_over_denominator = mp.pi / denominator

# Calculate square root of the result
result = mp.sqrt(pi_over_denominator)

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))