import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf('0.25'))

# Square the Gamma function value
gamma_squared = gamma_1_4 ** 2

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the constant factor: Gamma(1/4)^2 / sqrt(pi)
constant_factor = gamma_squared / sqrt_pi

# Compute the Bessel function J0 at 1
j0_1 = mp.besselj(0, 1)

# Multiply to get the final result
result = constant_factor * j0_1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))