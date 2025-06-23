import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Calculate pi squared divided by 6
term = pi_squared / 6

# Subtract 1 from the term to get the result
result = term - 1

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))