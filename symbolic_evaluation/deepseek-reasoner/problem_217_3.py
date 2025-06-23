import mpmath as mp
mp.dps = 15

# Calculate components of the numerator
sqrt_pi = mp.sqrt(mp.pi)  # Square root of pi
gamma_14 = mp.gamma(mp.mpf(1)/4)  # Gamma(1/4)
gamma_squared = gamma_14 ** 2  # Square of Gamma(1/4)
numerator = sqrt_pi * gamma_squared  # Combine numerator components

# Calculate denominator 2^(5/2)
denominator = mp.power(2, mp.mpf(5)/2)

# Final calculation
result = numerator / denominator

print(mp.nstr(result, n=10))