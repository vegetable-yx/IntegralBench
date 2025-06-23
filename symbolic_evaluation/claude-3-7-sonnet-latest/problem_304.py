import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Calculate the denominator
denominator = 108

# Compute the result: π² / 108
result = pi_squared / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))