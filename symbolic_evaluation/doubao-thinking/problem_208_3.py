import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi squared
pi_squared = mp.pi**2

# Calculate pi to the fourth power
pi_fourth = pi_squared**2

# Compute each term of the expression separately
term1 = pi_fourth / 192
term2 = pi_squared / 16
term3 = mp.mpf(1)/4

# Combine terms to get final result
result = term1 - term2 + term3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))