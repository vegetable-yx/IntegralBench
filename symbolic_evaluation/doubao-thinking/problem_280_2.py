import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each component of the expression
sqrt6 = mp.sqrt(6)  # Compute sqrt(6)
pi_sqrt6_over4 = (mp.pi * sqrt6) / 4  # First term: π*sqrt(6)/4

cosh_term = mp.cosh(1.5)  # Compute cosh(3/2)
bessel_term = mp.besseli(0, 1.5)  # Compute modified Bessel I_0(3/2)

# Combine all components
result = pi_sqrt6_over4 * cosh_term * bessel_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))