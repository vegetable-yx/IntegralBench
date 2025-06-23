import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate e^2 using exponential function
e_squared = mp.exp(2)

# Add 1 to e^2
numerator = e_squared + 1

# Multiply by 1/4 to get the final result
result = numerator / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))