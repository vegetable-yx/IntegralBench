import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi raised to the fourth power
pi_fourth = mp.pi**4

# Divide by 16 to get the result
result = pi_fourth / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))