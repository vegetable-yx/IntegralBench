import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 2^(5/4)
two_to_5_4 = mp.power(2, mp.mpf(5)/4)

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(3/4) and square it
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_squared = gamma_3_4 ** 2

# Multiply all components together
result = two_to_5_4 * sqrt_pi * gamma_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))