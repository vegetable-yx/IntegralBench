import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square the π value
pi_squared = mp.power(pi_val, 2)

# Compute the final result (3π²/16)
result = (3 * pi_squared) / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))