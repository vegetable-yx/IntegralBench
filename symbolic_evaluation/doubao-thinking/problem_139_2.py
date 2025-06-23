import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate cosh(2)
cosh_val = mp.cosh(2)

# Subtract 1 from cosh(2)
cosh_minus_one = cosh_val - 1

# Multiply by pi to get the result
result = mp.pi * cosh_minus_one

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))