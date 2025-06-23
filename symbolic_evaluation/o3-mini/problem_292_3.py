import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_power8 = gamma_val**8

# Compute pi squared
pi_sq = mp.pi**2

# Multiply pi squared by 128
denominator = 128 * pi_sq

# Divide the numerator by the denominator
result = gamma_power8 / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))