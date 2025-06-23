import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate e squared (e^2)
e_squared = mp.exp(2)

# Calculate numerator: e^2 - 1
numerator = e_squared - 1

# Compute final result: (e^2 - 1) / 4
result = numerator / 4

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))