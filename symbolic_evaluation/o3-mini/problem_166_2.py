import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Define pi constant from mpmath
pi_constant = mp.pi

# Compute the expression pi/4
result = pi_constant / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))