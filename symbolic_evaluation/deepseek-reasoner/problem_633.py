import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute ζ(3) using Riemann zeta function
zeta_3 = mp.zeta(3)

# Calculate the first term: (7/16)ζ(3)
term1 = mp.mpf(7)/16 * zeta_3

# Calculate π²
pi_squared = mp.pi**2

# Calculate the second term: (π²/8)ln(2)
term2 = (pi_squared / 8) * mp.log(2)

# Combine terms for final result
result = term1 - term2

# Print with 10 decimal precision
print(mp.nstr(result, n=10))