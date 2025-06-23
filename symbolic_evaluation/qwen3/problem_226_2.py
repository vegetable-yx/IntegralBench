import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_val = mp.pi

# Square the π value
pi_squared = mp.power(pi_val, 2)

# Divide the squared π by 2
result = mp.fdiv(pi_squared, 2)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))