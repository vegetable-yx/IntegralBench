import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute Gamma(3/4) using the gamma function
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Compute Gamma(5/4) using the gamma function
gamma_54 = mp.gamma(mp.mpf(5)/4)

# Multiply the two gamma values to get the result
result = gamma_34 * gamma_54

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))