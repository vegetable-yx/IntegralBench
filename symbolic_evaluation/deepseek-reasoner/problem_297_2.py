import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Compute the first term: pi^2 / 192
term1 = pi_squared / 192

# Compute pi^4 by squaring pi_squared
pi_fourth = pi_squared ** 2

# Compute the second term: pi^4 / 6144
term2 = pi_fourth / 6144

# Sum the two terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))