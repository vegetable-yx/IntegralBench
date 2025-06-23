import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute gamma(1/4)
gamma_quarter = mp.gamma(0.25)

# Raise gamma(1/4) to the 4th power
gamma_quarter_p4 = gamma_quarter**4

# Compute the denominator: 16 * sqrt(2 * pi)
denom = 16 * mp.sqrt(2 * mp.pi)

# Calculate the final result
result = gamma_quarter_p4 / denom

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))