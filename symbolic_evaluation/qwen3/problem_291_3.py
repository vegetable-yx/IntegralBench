import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 4th power
gamma_power = gamma_1_4**4

# Calculate the denominator 32*pi
denominator = 32 * mp.pi

# Compute the final result
result = gamma_power / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))