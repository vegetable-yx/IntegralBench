import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate components of the exponent
sqrt_42 = mp.sqrt(42)
exponent = 14 + 2 * sqrt_42

# Calculate the base (π/4)
base = mp.pi / 4

# Compute the base raised to the exponent
numerator = base ** exponent

# Calculate the denominator (14 + 2√42)
denominator = 14 + 2 * sqrt_42

# Final result calculation
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))