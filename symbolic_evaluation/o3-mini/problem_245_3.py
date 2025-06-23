import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(1/4)

# Raise Gamma(1/4) to the 8th power
gamma_1_4_power8 = gamma_1_4 ** 8

# Calculate the numerator: 256 * pi^2
numerator = 256 * pi_sq

# Compute the final result: numerator / gamma_1_4_power8
result = numerator / gamma_1_4_power8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))