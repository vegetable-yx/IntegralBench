import mpmath as mp

# Set the decimal places for internal precision
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 192 to get the result
result = pi_squared / 192

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))