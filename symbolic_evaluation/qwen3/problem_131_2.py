import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute Gamma(3/4) and square it
gamma_3_4 = mp.gamma(3/4)
gamma_squared = gamma_3_4 ** 2

# Compute 2^(3/4)
two_power = mp.power(2, 3/4)

# Combine components to calculate the final result
result = (sqrt_pi / gamma_squared) * two_power

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))