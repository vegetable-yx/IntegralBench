import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 96 to get the result
result = pi_cubed / 96

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))