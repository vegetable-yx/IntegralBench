import mpmath as mp

# Set internal decimal precision to 15 for sufficient accuracy
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 24 to obtain the result
result = pi_cubed / 24

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))