import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the denominator
denominator = 2019

# Compute pi divided by 2019
pi_over_denominator = mp.pi / denominator

# Calculate the square root of (pi/2019)
result = mp.sqrt(pi_over_denominator)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))