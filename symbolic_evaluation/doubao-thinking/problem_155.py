import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π (using mpmath's constant for pi)
pi_val = mp.pi

# Square π
pi_squared = pi_val ** 2

# Divide the result by 8
result = pi_squared / 8

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))