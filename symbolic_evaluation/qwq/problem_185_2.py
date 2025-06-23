import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Square the value of π
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 32
result = mp.fdiv(pi_squared, 32)

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))