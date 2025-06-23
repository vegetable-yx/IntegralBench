import mpmath as mp
mp.dps = 15

# Calculate sqrt(2) using mpmath's square root function
sqrt2 = mp.sqrt(2)

# Compute the numerator: 4 * sqrt(2) * pi
numerator = 4 * sqrt2 * mp.pi

# Calculate Gamma(1/4) using mpmath's gamma function
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma(1/4) value for denominator
gamma_squared = gamma_1_4 ** 2

# Compute final result by dividing numerator by squared gamma value
result = numerator / gamma_squared

# Print result with 10 decimal precision using mpmath's nstr
print(mp.nstr(result, n=10))