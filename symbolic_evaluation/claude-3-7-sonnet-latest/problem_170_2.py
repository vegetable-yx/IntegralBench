import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π (pi) using mpmath constant
pi_val = mp.pi

# Calculate π squared
pi_squared = pi_val ** 2

# Divide by 16 to get the final result
result = pi_squared / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))