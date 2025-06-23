import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute sin(2.0)
sin_val = mp.sin(2.0)

# Compute cos(2.0)
cos_val = mp.cos(2.0)

# Calculate (sin(2.0)/2.0)
term1 = sin_val / 2.0

# Calculate (sin(2.0)/2.0 - cos(2.0))
numerator = term1 - cos_val

# Compute denominator: 16 * sqrt(pi)
denominator = 16 * mp.sqrt(mp.pi)

# Final result: numerator / denominator
result = numerator / denominator

# Print result to 10 decimal places
print(mp.nstr(result, n=10))