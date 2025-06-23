import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate Gamma(1/2) - equivalent to sqrt(π)
gamma_half = mp.gamma(mp.mpf(1)/2)

# Calculate Gamma(3/4)
gamma_three_fourth = mp.gamma(mp.mpf(3)/4)

# Compute the final result
result = sqrt2 * gamma_half / gamma_three_fourth

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))