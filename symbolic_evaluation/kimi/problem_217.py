import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the Gamma function result
gamma_squared = gamma_val ** 2

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute denominator part: Gamma^2 / sqrt(pi)
denominator_part = gamma_squared / sqrt_pi

# Calculate modified Bessel function I0(2)
bessel_part = mp.besseli(0, 2)

# Combine components for final result
result = denominator_part * bessel_part

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))