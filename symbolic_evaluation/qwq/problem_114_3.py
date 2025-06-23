import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Divide π squared by 8
pi_squared_over_8 = pi_squared / 8

# Apply the negative sign to get final result
result = -pi_squared_over_8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))