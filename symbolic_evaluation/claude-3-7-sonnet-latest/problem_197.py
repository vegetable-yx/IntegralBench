import mpmath as mp

# Set internal decimal precision to 15 for accurate results
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide pi squared by 16
term1 = pi_squared / 16

# Calculate 1/4
term2 = mp.mpf(1) / 4

# Add the two terms together
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))