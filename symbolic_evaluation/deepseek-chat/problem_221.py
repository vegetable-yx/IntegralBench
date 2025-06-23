import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant 3
three = mp.mpf(3)

# Define the constant 16
sixteen = mp.mpf(16)

# Calculate the numerator: 3 * π
numerator = three * mp.pi

# Compute the final result: (3π)/16
result = numerator / sixteen

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))