import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the value of π
pi_squared = mp.power(pi_value, 2)

# Divide by 8 to get the final result
result = pi_squared / 8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))