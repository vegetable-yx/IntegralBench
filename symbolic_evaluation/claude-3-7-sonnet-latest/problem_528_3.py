import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the mathematical constant e
e_constant = mp.e

# Calculate the expression: 1 - e
result = 1 - e_constant

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))