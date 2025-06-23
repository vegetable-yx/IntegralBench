import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute pi using mpmath's constant
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Divide by 96 to get the result
result = pi_cubed / 96

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))