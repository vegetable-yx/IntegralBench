import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the constant factors
sqrt2 = mp.sqrt(2)  # sqrt(2)
sqrt_pi = mp.sqrt(mp.pi)  # sqrt(pi)
factor = sqrt2 / (2 * sqrt_pi)  # \frac{\sqrt{2}}{2\sqrt{\pi}}

# Compute Gamma(3/4) and square it
gamma_val = mp.gamma(mp.mpf(3)/4)  # \Gamma(3/4)
gamma_sq = gamma_val ** 2  # \Gamma(3/4)^2

# Evaluate Bessel functions at sqrt(2)
arg = sqrt2  # argument is sqrt(2)
J_neg = mp.besselj(-0.25, arg)  # J_{-1/4}(sqrt(2))
J_pos = mp.besselj(0.25, arg)   # J_{1/4}(sqrt(2))

# Compute the difference of Bessel functions
bessel_diff = J_neg - J_pos  # [J_{-1/4}(sqrt(2)) - J_{1/4}(sqrt(2))]

# Combine all parts: factor * gamma_sq * bessel_diff
result = factor * gamma_sq * bessel_diff

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))