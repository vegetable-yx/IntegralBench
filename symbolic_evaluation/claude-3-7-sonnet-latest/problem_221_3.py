import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant 3π
numerator = 3 * mp.pi

# Divide the result by 16 to obtain the final value
result = numerator / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))