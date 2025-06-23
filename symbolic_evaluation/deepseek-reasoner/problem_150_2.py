import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π^(3/2)
pi_power = mp.pi ** (3/2)

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate Gamma(3/4)
gamma_3_4 = mp.gamma(3/4)

# Square the Gamma(3/4) value
gamma_squared = gamma_3_4 ** 2

# Calculate denominator: sqrt(2) * [Gamma(3/4)]^2
denominator = sqrt2 * gamma_squared

# Compute final result by dividing π^(3/2) by denominator
result = pi_power / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))