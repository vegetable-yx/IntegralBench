import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 4th power
gamma_power4 = gamma_val**4

# Calculate the denominator: 4 * sqrt(2*pi)
denominator = 4 * mp.sqrt(2 * mp.pi)

# Compute the final result: [Gamma(1/4)^4] / [4*sqrt(2*pi)]
result = gamma_power4 / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))