import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate arcsin(1/4)
a = mp.asin(1/4)

# Compute first term: (π/16) * arcsin(1/4)
term1 = (mp.pi / 16) * a

# Compute second term: 0.5 * (arcsin(1/4))^2
term2 = 0.5 * a**2

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))