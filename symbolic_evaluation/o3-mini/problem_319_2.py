import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of parameter 'a' (example value, can be changed)
a = 1.0

# Precompute common constants
sqrt_pi = mp.sqrt(mp.pi)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)

# Calculate the constant coefficient: sqrt(pi) * Gamma(3/4) / (2 * Gamma(5/4))
constant_factor = (sqrt_pi * gamma_3_4) / (2 * gamma_5_4)

# Compute the argument for the hypergeometric functions: a^2/4
z = (a**2) / 4

# Calculate first hypergeometric function: 1F2(1/2; 3/4, 5/4; z)
hyper1 = mp.hyper([mp.mpf(1)/2], [mp.mpf(3)/4, mp.mpf(5)/4], z)

# Calculate second hypergeometric function: 1F2(-1/2; 1/4, 3/4; z)
hyper2 = mp.hyper([mp.mpf(-1)/2], [mp.mpf(1)/4, mp.mpf(3)/4], z)

# Compute the bracketed expression: (a/2)*hyper1 - hyper2
bracket = (a/2)*hyper1 - hyper2

# Multiply by the constant factor to get the final result
result = constant_factor * bracket

# Print result to 10 decimal places
print(mp.nstr(result, n=10))