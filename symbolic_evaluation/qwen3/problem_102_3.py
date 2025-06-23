import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Divide by 36 to get the final result
result = pi_squared / 36

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))