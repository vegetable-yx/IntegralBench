import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 192 to obtain the result
result = pi_cubed / 192

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))