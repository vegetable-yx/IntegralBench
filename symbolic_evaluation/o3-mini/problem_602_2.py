import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi raised to the fourth power
pi_val = mp.pi
pi_squared = pi_val ** 2
pi_fourth = pi_squared ** 2

# Divide by 120 to get the final result
result = pi_fourth / 120

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))