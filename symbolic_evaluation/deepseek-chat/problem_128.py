import mpmath as mp

# Set the decimal places of precision for internal calculations
mp.dps = 15

# The analytical expression is pi, which is a fundamental constant
# Assign the constant pi to the result variable
result = mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))