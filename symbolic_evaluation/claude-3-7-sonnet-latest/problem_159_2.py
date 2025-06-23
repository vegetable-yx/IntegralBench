import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the hyperbolic sine of 4
sinh_value = mp.sinh(4)

# Multiply by 8 to get the final result
result = 8 * sinh_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))