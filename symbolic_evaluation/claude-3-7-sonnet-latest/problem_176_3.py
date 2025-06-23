import mpmath as mp

# Set the decimal places for internal precision
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 8 to get the result
result = pi_cubed / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))