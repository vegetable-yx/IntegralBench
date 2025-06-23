import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute Gamma(3/4)
gamma_3_4 = mp.gamma(3/4)

# Square the Gamma(3/4) value
gamma_sq = gamma_3_4 ** 2

# Compute the Bessel function J0 at 0.5
j0_val = mp.besselj(0, 0.5)

# Combine all parts: 2 * sqrt(pi) * [Gamma(3/4)]^2 * J0(0.5)
result = 2 * sqrt_pi * gamma_sq * j0_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))