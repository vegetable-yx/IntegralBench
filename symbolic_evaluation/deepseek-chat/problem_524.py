import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute e^2 (exponential function)
e_squared = mp.exp(2)

# Calculate numerator: e^2 + 1
numerator = e_squared + 1

# Final result: (e^2 + 1) divided by 4
result = numerator / 4

# Print result to 10 decimal places
print(mp.nstr(result, n=10))