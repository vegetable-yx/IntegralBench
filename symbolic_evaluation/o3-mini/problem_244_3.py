import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise Gamma(1/4) to the 8th power
gamma_val_8 = gamma_val**8

# Compute pi squared
pi_sq = mp.pi**2

# Multiply 128 by pi squared
denominator = 128 * pi_sq

# Divide the Gamma part by the denominator
result = gamma_val_8 / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))