import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi using mpmath constant
pi_val = mp.pi

# Compute pi raised to the fourth power
pi_fourth = pi_val ** 4

# Divide the result by 128 to get the final value
result = pi_fourth / 128

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))