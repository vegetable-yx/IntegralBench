import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma1 = mp.gamma(mp.mpf('1/4'))

# Compute Gamma(3/4)
gamma2 = mp.gamma(mp.mpf('3/4'))

# Multiply the Gamma values and then by 1/4
product = gamma1 * gamma2
result = mp.mpf('0.25') * product

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))