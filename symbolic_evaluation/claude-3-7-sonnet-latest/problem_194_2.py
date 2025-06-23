import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Compute the result by dividing by 24
result = pi_squared / 24

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))