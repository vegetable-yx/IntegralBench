import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: 2^(3/4)
factor = mp.power(2, 3/4)

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Evaluate Gamma(3/4)
gamma_val = mp.gamma(3/4)

# Compute the fraction: sqrt(pi) / Gamma(3/4)
fraction = sqrt_pi / gamma_val

# Multiply to get the final result
result = factor * fraction

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))