import mpmath as mp

# Set internal decimal precision to 15 digits for intermediate calculations
mp.dps = 15

# Compute pi value
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Divide by 24 to get the result
result = pi_cubed / 24

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))