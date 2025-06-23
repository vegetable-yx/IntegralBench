import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π (pi) using mpmath's constant
pi_val = mp.pi

# Compute π raised to the power of 3
pi_cubed = mp.power(pi_val, 3)

# Divide the result by 24 to get the final value
result = pi_cubed / 24

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))