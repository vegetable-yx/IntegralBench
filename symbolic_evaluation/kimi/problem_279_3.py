import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate hyperbolic cosine of 1
cosh_1 = mp.cosh(1)

# Calculate π/2
pi_over_2 = mp.pi / 2

# Multiply π/2 with cosh(1)
product = pi_over_2 * cosh_1

# Apply negative sign to final result
result = -product

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))