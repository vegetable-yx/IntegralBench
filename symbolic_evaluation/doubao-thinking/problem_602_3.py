import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi raised to the fourth power
pi_to_fourth = mp.pi ** 4

# Divide by 120 to get the result
result = pi_to_fourth / 120

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))