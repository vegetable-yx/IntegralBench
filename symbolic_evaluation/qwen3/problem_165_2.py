import mpmath as mp
mp.dps = 15  # Set decimal precision for internal calculations

# Calculate Struve H function of order 0 at z=2
struve_value = mp.struveh(0, 2)

# Compute π/2
pi_half = mp.pi / 2

# Multiply components to get final result
result = pi_half * struve_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))