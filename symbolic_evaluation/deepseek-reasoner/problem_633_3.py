import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute ζ(3) using Riemann zeta function
zeta_3 = mp.zeta(3)

# Calculate first term: (7/16) * ζ(3)
term1 = mp.fdiv(7, 16) * zeta_3

# Compute π²
pi_squared = mp.power(mp.pi, 2)

# Compute ln(2)
ln2 = mp.log(2)

# Calculate second term: (π²/8) * ln(2)
term2 = mp.fdiv(pi_squared, 8) * ln2

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))