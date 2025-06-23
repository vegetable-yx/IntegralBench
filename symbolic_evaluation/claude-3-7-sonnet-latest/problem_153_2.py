import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute pi using mpmath constant
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Divide by 24 to get the result
result = pi_cubed / 24

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))