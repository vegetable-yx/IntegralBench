import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Compute the first term: pi^2 divided by 16
term1 = pi_squared / 16

# Compute the second term: 1/2
term2 = mp.mpf(1) / 2

# Combine terms to get final result
result = term1 - term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))