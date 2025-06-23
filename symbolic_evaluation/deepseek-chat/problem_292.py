import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath constant
pi_val = mp.pi

# Compute pi cubed: π^3
pi_cubed = pi_val ** 3

# Divide by 8 to get final result
result = pi_cubed / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))