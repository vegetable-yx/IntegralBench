import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant: (19 * π) / 512
numerator = 19 * mp.pi  # Multiply 19 by π
result = numerator / 512  # Divide by 512

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))