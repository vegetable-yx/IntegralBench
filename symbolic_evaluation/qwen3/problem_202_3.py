import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sin(1) using mpmath's sine function
sin_value = mp.sin(1)

# Multiply by 2 to get the final result
result = 2 * sin_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))