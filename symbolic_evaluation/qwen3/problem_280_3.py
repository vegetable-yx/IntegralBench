import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Compute the ratio sqrt(pi)/Gamma(3/4)
ratio = sqrt_pi / gamma_3_4

# Square the ratio
ratio_squared = ratio ** 2

# Calculate hyperbolic cosine of 3
cosh3 = mp.cosh(3)

# Combine all components for final result
result = sqrt3 * ratio_squared * cosh3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))