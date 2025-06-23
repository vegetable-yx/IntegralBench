import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute the value of 1 divided by square root of pi
result = 1 / sqrt_pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))