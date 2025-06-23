import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/4)
gamma_one_fourth = mp.gamma(mp.mpf(1)/4)

# Calculate gamma(3/4)
gamma_three_fourth = mp.gamma(mp.mpf(3)/4)

# Multiply the gamma values and scale by 1/4
result = gamma_one_fourth * gamma_three_fourth * (mp.mpf(1)/4)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))