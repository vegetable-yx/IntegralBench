import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_value = mp.pi
pi_squared = pi_value ** 2

# Assign the result
result = pi_squared

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))