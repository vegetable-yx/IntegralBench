import mpmath as mp

# Set the internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# The analytical expression is the constant π
# Assign the value of π to a variable
pi_value = mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(pi_value, n=10))