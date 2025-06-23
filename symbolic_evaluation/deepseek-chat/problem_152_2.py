import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 4 to obtain the result
result = pi_squared / 4

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))