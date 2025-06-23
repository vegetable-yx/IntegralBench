import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sinh(5) using mpmath
sinh_value = mp.sinh(5)

# Multiply by 25
numerator = 25 * sinh_value

# Divide by 4 to get the final result
result = numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))