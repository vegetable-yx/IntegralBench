import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Define the constant pi
pi_value = mp.pi

# Multiply pi by 2 to get the result
result = 2 * pi_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))