import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 16 to obtain the final result
result = pi_squared / 16

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))