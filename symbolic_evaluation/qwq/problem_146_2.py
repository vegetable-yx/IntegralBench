import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π^3
pi_cubed = mp.pi ** 3

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Calculate the denominator 8*sqrt(2)
denominator = 8 * sqrt_2

# Compute the final result
result = pi_cubed / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))