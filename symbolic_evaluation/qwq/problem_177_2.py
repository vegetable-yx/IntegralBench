import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the value of π
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 3
result = pi_squared / 3

# Print the result with 10 decimal places using mpmath's string formatting
print(mp.nstr(result, n=10))