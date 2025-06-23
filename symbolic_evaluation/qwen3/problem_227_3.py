import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi to the fourth power
pi_fourth = mp.pi ** 4

# Divide by 1440
result = pi_fourth / 1440

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))