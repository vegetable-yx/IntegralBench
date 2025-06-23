import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_val = mp.pi

# Cube the value of π
pi_cubed = pi_val ** 3

# Divide the cubed value by 32
result = pi_cubed / 32

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))