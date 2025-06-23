import mpmath as mp

# Set internal decimal places for calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 16 to get the result
result = pi_squared / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))