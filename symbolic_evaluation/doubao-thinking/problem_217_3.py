import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate sqrt(2*pi)
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Calculate 2^(1/4)
two_to_quarter = mp.power(2, mp.mpf(1)/4)

# Calculate Gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf(1)/4)

# Calculate Bessel function J_{1/4}(1)
bessel_j_quarter = mp.besselj(mp.mpf(1)/4, 1)

# Combine all components
result = sqrt_2pi * two_to_quarter * gamma_quarter * bessel_j_quarter

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))