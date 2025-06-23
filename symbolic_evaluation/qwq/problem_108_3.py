import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide by 5 to get final result
result = pi_squared / 5

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))