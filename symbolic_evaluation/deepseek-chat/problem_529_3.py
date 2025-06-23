import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# The analytical expression is -π
# Assign the constant π to a variable
pi_value = mp.pi

# Negate the value of π
result = -pi_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))