import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 480 to get the final result
result = pi_cubed / 480

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))