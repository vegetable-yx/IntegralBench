import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sin(1) with mpmath precision
sin_1 = mp.sin(1)

# Calculate cos(1) with mpmath precision
cos_1 = mp.cos(1)

# Compute 6*sin(1) term
term1 = 6 * sin_1

# Compute 4*cos(1) term
term2 = 4 * cos_1

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))