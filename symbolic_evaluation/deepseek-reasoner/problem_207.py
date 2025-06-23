import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the denominator
denominator = 8

# Compute pi divided by 8
pi_over_8 = mp.pi / denominator

# Take the square root of (pi/8)
result = mp.sqrt(pi_over_8)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))