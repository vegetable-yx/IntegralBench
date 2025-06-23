import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate pi squared
pi_val = mp.pi
pi_squared = pi_val ** 2

# Divide by 8 to get the result
result = pi_squared / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))