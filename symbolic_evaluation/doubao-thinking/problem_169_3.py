import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 4 to get final result
result = pi_squared / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))