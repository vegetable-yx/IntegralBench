import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate Gamma(3/4)
gamma_val = mp.gamma(mp.mpf(3)/4)

# Calculate modified Bessel function I_{3/4}(4)
bessel_val = mp.besseli(mp.mpf(3)/4, 4)

# Compute the product of π and Gamma(3/4)
pi_gamma = mp.pi * gamma_val

# Multiply by Bessel function result
numerator = pi_gamma * bessel_val

# Calculate denominator 2^(5/4)
denominator = mp.power(2, mp.mpf(5)/4)

# Compute final result
result = numerator / denominator

# Print with 10 decimal precision
print(mp.nstr(result, n=10))