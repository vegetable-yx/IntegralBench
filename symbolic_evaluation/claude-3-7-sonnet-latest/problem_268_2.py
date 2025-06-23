import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi raised to the fourth power
pi_fourth = mp.power(pi_val, 4)

# Divide the result by 96
result = pi_fourth / 96

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))