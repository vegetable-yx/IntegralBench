import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 36 to get the result
result = pi_squared / 36

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))