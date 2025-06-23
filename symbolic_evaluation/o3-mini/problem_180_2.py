import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute gamma(3/4)
gamma_34 = mp.gamma(3/4)

# Square the gamma value
gamma_sq = gamma_34 ** 2

# Compute numerator: sqrt(2) * [gamma(3/4)]^2
numerator = mp.sqrt(2) * gamma_sq

# Compute denominator: 4 * sqrt(pi)
denominator = 4 * mp.sqrt(mp.pi)

# Compute the argument for Bessel functions: sqrt(2)
arg = mp.sqrt(2)

# Compute Bessel functions J_{-1/4}(sqrt(2)) and J_{1/4}(sqrt(2))
J_neg_quarter = mp.besselj(-1/4, arg)
J_pos_quarter = mp.besselj(1/4, arg)

# Compute the difference: J_{-1/4}(sqrt(2)) - J_{1/4}(sqrt(2))
bessel_diff = J_neg_quarter - J_pos_quarter

# Combine all parts: [numerator / denominator] * bessel_diff
result = (numerator / denominator) * bessel_diff

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))