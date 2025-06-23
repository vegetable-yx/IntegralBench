import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the value of pi
pi_value = mp.pi

# Compute pi cubed
pi_cubed = pi_value ** 3

# Divide by 8 to get the final result
result = pi_cubed / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))