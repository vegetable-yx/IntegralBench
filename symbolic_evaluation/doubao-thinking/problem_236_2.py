import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute Gamma(5/4)
gamma_5_4 = mp.gamma(5/4)

# Compute Gamma(3/4)
gamma_3_4 = mp.gamma(3/4)

# Calculate the final result using exact formula
result = (mp.pi * gamma_5_4) / gamma_3_4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))