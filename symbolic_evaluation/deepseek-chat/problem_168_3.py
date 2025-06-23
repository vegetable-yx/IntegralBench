import mpmath as mp

# Set the internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi cubed: π raised to the power of 3
pi_cubed = mp.pi ** 3

# Divide pi cubed by 4 to obtain the final result
result = pi_cubed / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))