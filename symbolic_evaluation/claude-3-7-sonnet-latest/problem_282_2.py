import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the Gamma value
gamma_sq = gamma_val ** 2

# Compute the denominator: 2 * sqrt(pi)
denominator = 2 * mp.sqrt(mp.pi)

# Compute the fraction: Gamma^2(1/4) / (2*sqrt(pi))
fraction = gamma_sq / denominator

# Compute the modified Bessel function I_0(4)
bessel_val = mp.besseli(0, 4)

# Multiply to get the final result
result = fraction * bessel_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))