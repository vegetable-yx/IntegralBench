import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_quarter_8 = gamma_quarter**8

# Calculate the denominator: 6144 * sqrt(2*pi)
denominator = 6144 * mp.sqrt(2 * mp.pi)

# Compute the final result
result = gamma_quarter_8 / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))