import mpmath as mp
mp.dps = 15

# Compute Gamma(3/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Square the Gamma function value
gamma_squared = gamma_34 ** 2

# Calculate hyperbolic cosine of 2
cosh_2 = mp.cosh(2)

# Combine components for final result
result = (4 / gamma_squared) * cosh_2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))