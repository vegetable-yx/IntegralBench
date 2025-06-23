import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf(1)/4)

# Raise gamma(1/4) to the 4th power
gamma_quarter_4 = gamma_quarter**4

# Compute the denominator: 4 * sqrt(2 * pi)
denominator = 4 * mp.sqrt(2 * mp.pi)

# Divide to get the final result
result = gamma_quarter_4 / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))