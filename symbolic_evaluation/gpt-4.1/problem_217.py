import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(0.25)

# Square the Gamma(1/4) value
gamma_squared = gamma_val ** 2

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the prefactor: Gamma(1/4)^2 / sqrt(pi)
prefactor = gamma_squared / sqrt_pi

# Evaluate the hypergeometric function 1F2(1/4; 1/4, 1/4; -1)
hyper_term = mp.hyper([0.25], [0.25, 0.25], -1)

# Multiply prefactor by the hypergeometric function result
result = prefactor * hyper_term

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))