import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide by 8 to get the final result
result = pi_squared / 8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))