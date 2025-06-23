import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the denominator
denominator = 2019

# Compute the fraction π/2019
pi_over_denominator = mp.pi / denominator

# Calculate the square root of the fraction
result = mp.sqrt(pi_over_denominator)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))