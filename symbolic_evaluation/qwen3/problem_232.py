import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 2^(3/2)
two_power = mp.power(2, 1.5)

# Compute Gamma(3/4)
gamma_val = mp.gamma(0.75)

# Square the Gamma value
gamma_squared = gamma_val ** 2

# Calculate the denominator sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Combine all components for the final result
result = (two_power * gamma_squared) / sqrt_pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))