import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Define the mathematical constant e
e_val = mp.e

# Calculate the expression: e * (3 - e)
term = 3 - e_val  # Compute (3 - e)
result = e_val * term  # Multiply by e

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))