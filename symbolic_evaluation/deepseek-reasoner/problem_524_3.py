import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate e squared using mpmath exponential function
e_squared = mp.exp(2)

# Compute the numerator: e^2 + 1
numerator = e_squared + 1

# Divide by 4 to get the final result
result = numerator / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))