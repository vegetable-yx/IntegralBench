import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf('0.25'))

# Square the Gamma function value
gamma_sq = gamma_val**2

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Multiply sqrt(2) by the squared Gamma value
numerator = sqrt2 * gamma_sq

# Compute sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Multiply 3 by sqrt(pi) to get the denominator
denominator = 3 * sqrt_pi

# Divide numerator by denominator to get the result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))