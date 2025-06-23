import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Assign the constant pi value
pi_val = mp.pi

# Compute the negative of pi
result = -pi_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))