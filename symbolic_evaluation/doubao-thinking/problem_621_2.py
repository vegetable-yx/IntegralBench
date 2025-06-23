import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the value of pi
pi_val = mp.pi

# Multiply pi by -1/2 to get the result
result = -pi_val / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))