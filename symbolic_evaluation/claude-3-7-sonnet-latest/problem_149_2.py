import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute Gamma(1/4) - gamma function at 1/4
gamma_quarter = mp.gamma(0.25)

# Square the Gamma(1/4) value
gamma_squared = gamma_quarter ** 2

# Multiply sqrt(pi) by the squared gamma value
result = sqrt_pi * gamma_squared

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))