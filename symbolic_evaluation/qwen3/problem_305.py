import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square the π value
pi_squared = mp.power(pi_val, 2)

# Divide by 48 to get the final result
result = pi_squared / 48

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))