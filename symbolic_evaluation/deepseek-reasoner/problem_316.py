import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate fundamental constants
sqrt2 = mp.sqrt(2)
log2 = mp.log(2)
pi = mp.pi
zeta3 = mp.zeta(3)  # Riemann zeta function at 3

# Compute first term components
term1_coeff = 4 * sqrt2
term1 = term1_coeff * pi * log2

# Compute second term components
term2_coeff = (7 * sqrt2) / 2
term2 = term2_coeff * zeta3

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))