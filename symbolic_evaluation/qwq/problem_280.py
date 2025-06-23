import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Gamma(1/4) and square it
gamma_14 = mp.gamma(mp.mpf(1)/4)
gamma_14_squared = gamma_14 ** 2

# Calculate sqrt(3)
sqrt3 = mp.sqrt(3)

# Calculate numerator: sqrt(3) * Gamma(1/4)^2
numerator = sqrt3 * gamma_14_squared

# Calculate Gamma(3/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate denominator: sqrt(2) * Gamma(3/4)
denominator = sqrt2 * gamma_34

# Compute final result
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))