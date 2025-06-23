import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate components of the numerator
# sqrt(2 * pi)
sqrt_2pi = mp.sqrt(2 * mp.pi)
# exp(-1/2)
exp_minus_half = mp.exp(-0.5)
# Gamma(1/4)
gamma_quarter = mp.gamma(0.25)
# Modified Bessel function I_{-1/4}(1/2)
bessel_minus_quarter = mp.besseli(-0.25, 0.5)

# Combine numerator: sqrt(2pi) * e^{-1/2} * Gamma(1/4) * I_{-1/4}(1/2)
numerator = sqrt_2pi * exp_minus_half * gamma_quarter * bessel_minus_quarter

# Calculate denominator: 4 * Gamma(3/4)
gamma_three_quarters = mp.gamma(0.75)
denominator = 4 * gamma_three_quarters

# Compute final result
result = numerator / denominator

# Print result to 10 decimal places
print(mp.nstr(result, n=10))