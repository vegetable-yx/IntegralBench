import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate 3 times pi using high-precision arithmetic
three_pi = 3 * mp.pi

# Store the final value
result = three_pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))