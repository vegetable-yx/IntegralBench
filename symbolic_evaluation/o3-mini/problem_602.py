import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate pi to the fourth power
pi_fourth = mp.pi ** 4

# Divide by 120 to get the final result
result = pi_fourth / 120

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))