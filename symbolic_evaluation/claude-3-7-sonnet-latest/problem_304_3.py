import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute the constant pi
pi_value = mp.pi

# Divide pi by 24 to get the result
result = pi_value / 24

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))