import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Square Gamma(1/4)
gamma_14_squared = gamma_14 ** 2

# Calculate Gamma(1/2)
gamma_12 = mp.gamma(mp.mpf(1)/2)

# Compute the fraction: Gamma(1/4)^2 / Gamma(1/2)
fraction = gamma_14_squared / gamma_12

# Multiply by pi/2
result = (mp.pi / 2) * fraction

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))