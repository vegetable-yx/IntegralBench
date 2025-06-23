import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate 2^(3/4)
two_power = mp.power(2, mp.mpf(3)/4)

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate numerator: 2^(3/4) * sqrt(pi)
numerator = two_power * sqrt_pi

# Calculate denominator: Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Compute final result
result = numerator / gamma_3_4

# Print result with 10 decimal places
print(mp.nstr(result, n=10))