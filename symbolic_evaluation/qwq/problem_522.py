import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the denominator
denominator = 2019

# Compute pi divided by 2019
pi_over_denominator = mp.pi / denominator

# Take the square root of the result
result = mp.sqrt(pi_over_denominator)

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))