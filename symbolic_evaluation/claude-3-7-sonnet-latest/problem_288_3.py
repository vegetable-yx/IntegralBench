import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate pi^3
pi_cubed = mp.pi ** 3

# Divide by 48 to get the result
result = pi_cubed / 48

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))