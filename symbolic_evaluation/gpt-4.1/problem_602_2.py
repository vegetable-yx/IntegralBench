import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi raised to the fourth power
pi_fourth = mp.pi ** 4

# Divide by 120 to get the final result
result = pi_fourth / 120

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))