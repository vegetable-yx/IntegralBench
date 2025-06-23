import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute pi to the current precision
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Divide pi cubed by 8 to get the result
result = pi_cubed / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))