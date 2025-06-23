import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute pi raised to the power of 3/2
pi_power = mp.pi ** (mp.mpf(3)/2

# Compute 2 raised to the power of 3/2
two_power = mp.power(2, mp.mpf(3)/2)

# Evaluate gamma function at 3/4
gamma_val = mp.gamma(mp.mpf(3)/4)

# Square the gamma value
gamma_sq = gamma_val ** 2

# Compute the denominator: 2^(3/2) * [gamma(3/4)]^2
denominator = two_power * gamma_sq

# Final result: pi^(3/2) / denominator
result = pi_power / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))