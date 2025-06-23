import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma(1/4) value
gamma_squared = gamma_1_4 ** 2

# Calculate denominator components: 2^(3/2) and pi
two_power = mp.power(2, mp.mpf(3)/2)
denominator = two_power * mp.pi

# Compute final result by dividing squared gamma by denominator
result = gamma_squared / denominator

# Print result to 10 decimal places
print(mp.nstr(result, n=10))