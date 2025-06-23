import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate numerator (π)
numerator = mp.pi

# Calculate denominator (√3)
denominator = mp.sqrt(3)

# Compute the final value π/√3
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))