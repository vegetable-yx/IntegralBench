import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the Gamma value
gamma_sq = gamma_val ** 2

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply sqrt(pi) by the squared Gamma value
numerator = sqrt_pi * gamma_sq

# Divide by 4 to get the final result
result = numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))