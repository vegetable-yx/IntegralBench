import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma function value
result = gamma_1_4 ** 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))