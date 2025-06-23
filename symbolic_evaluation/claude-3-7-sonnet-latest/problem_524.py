import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate e^2 using mpmath's exponential function
e_squared = mp.exp(2)

# Add 1 to the result
numerator = e_squared + 1

# Divide the numerator by 2 to get the final result
result = numerator / 2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))