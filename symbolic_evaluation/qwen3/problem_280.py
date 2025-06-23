import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate each component of the expression separately
sqrt_pi = mp.sqrt(mp.pi)  # Square root of pi
three_34 = mp.power(3, 3/4)  # 3^(3/4)
exp3 = mp.exp(3)  # e^3
gamma_34 = mp.gamma(3/4)  # Gamma function at 3/4
bessel_term = mp.besseli(-1/4, 3)  # Modified Bessel function I_{-1/4}(3)
sqrt_2 = mp.sqrt(2)  # Square root of 2

# Combine components according to the formula
numerator = sqrt_pi * three_34 * exp3 * gamma_34 * bessel_term
result = numerator / sqrt_2  # Final division by sqrt(2)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))