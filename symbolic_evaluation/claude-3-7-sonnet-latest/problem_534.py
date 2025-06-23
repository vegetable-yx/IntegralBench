import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Step 2: Multiply by 2 to get the final result
result = 2 * sqrt_pi

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))