import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_val = mp.pi

# Square the π value
pi_squared = mp.power(pi_val, 2)

# Divide by 72 to get the final result
result = pi_squared / 72

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))