import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute pi^4
pi = mp.pi
pi_to_fourth = pi**4

# Divide by 128 to get the final result
result = pi_to_fourth / 128

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))