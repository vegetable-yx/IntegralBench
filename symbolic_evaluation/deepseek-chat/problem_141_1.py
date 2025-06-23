import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant e
e_val = mp.e

# Compute e squared
e_squared = e_val**2

# Calculate numerator: e^2 - 1
numerator = e_squared - 1

# Calculate denominator: 4e
denominator = 4 * e_val

# Final result: (e^2 - 1)/(4e)
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))