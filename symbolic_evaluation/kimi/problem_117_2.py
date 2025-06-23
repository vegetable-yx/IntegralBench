import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 12 to get the result
result = pi_squared / 12

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))