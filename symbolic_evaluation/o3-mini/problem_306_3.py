import mpmath as mp

# Set internal decimal precision to 15 for accuracy
mp.dps = 15

# Calculate Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Calculate Gamma(5/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)

# Compute the ratio (Gamma(3/4) / Gamma(5/4))
ratio = gamma_3_4 / gamma_5_4

# Square the ratio to get the final result
result = ratio ** 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))