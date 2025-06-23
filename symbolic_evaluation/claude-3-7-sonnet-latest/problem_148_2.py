import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the result
result = gamma_val**2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))