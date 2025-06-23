import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 8
result = mp.fdiv(pi_squared, 8)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))