import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the multiplicative constant
constant = -3

# Get the exact value of π from mpmath
pi_value = mp.pi

# Compute the result: -3 * π
result = constant * pi_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))