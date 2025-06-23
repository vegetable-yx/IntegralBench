import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the calculated π
pi_squared = pi_value ** 2

# Divide by 6 to get the final result
result = pi_squared / 6

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))