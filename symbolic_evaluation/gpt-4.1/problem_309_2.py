import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the denominator: square root of 2
denominator = mp.sqrt(2)

# Compute the result: π divided by √2
result = mp.pi / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))