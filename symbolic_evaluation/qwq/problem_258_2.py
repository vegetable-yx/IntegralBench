import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate numerator: 2 * sqrt(pi)
numerator = 2 * mp.sqrt(mp.pi)

# Calculate denominator: e^(0.25)
denominator = mp.exp(0.25)

# Compute final result by dividing numerator by denominator
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))