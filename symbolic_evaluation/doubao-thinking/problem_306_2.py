import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π squared divided by 4
pi_squared = pi_value ** 2
result = pi_squared / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))