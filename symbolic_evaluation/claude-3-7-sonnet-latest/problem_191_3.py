import mpmath as mp

# Set the internal decimal precision to 15
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 64 to get the final result
result = pi_cubed / 64

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))