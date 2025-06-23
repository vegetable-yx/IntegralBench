import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/4)
gamma_quarter = mp.gamma(0.25)

# Raise gamma(1/4) to the 8th power
gamma_quarter_8 = gamma_quarter**8

# Compute pi squared
pi_sq = mp.pi**2

# Calculate the denominator: 128 * pi^2
denominator = 128 * pi_sq

# Divide numerator by denominator
result = gamma_quarter_8 / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))