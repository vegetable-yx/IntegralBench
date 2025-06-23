import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the constant pi from mpmath
pi_val = mp.pi

# Calculate the result: 4 divided by pi
result = 4 / pi_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))