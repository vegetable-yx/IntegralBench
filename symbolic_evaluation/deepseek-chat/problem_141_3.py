import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate the constant e (base of natural logarithm)
e_constant = mp.e

# Compute numerator: e^2 - 1
numerator = e_constant**2 - 1

# Compute denominator: 4 * e
denominator = 4 * e_constant

# Final result: (e^2 - 1) / (4e)
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))