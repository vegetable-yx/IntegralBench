import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate components of the expression
sqrt_pi = mp.sqrt(mp.pi)  # Square root of pi
gamma_1_4 = mp.gamma(1/4)  # Gamma function at 1/4
gamma_3_4 = mp.gamma(3/4)  # Gamma function at 3/4
bessel_term = mp.besselj(-1/4, 0.5)  # Bessel function of order -1/4 at 1/2

# Combine components according to the formula
numerator = sqrt_pi * gamma_1_4 * bessel_term
result = numerator / gamma_3_4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))