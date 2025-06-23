import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Cube the value of pi
pi_cubed = pi_val ** 3

# Divide by 8 to get the final result
result = pi_cubed / 8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))