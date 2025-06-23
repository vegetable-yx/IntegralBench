import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(3/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Compute denominator: 2^(1/2) * Gamma(3/4)
denominator = mp.sqrt(2) * gamma_34

# Compute the entire expression
result = sqrt_pi * gamma_14 / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))