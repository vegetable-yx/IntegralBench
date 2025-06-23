import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Compute modified Bessel function I_{1/4}(1)
bessel_val = mp.besseli(mp.mpf(1)/4, 1)

# Calculate the numerator: 2 * Gamma(1/4) * Bessel function
numerator = 2 * gamma_val * bessel_val

# Calculate denominator: square root of pi
denominator = mp.sqrt(mp.pi)

# Compute final result
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))