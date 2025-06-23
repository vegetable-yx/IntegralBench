import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Retrieve the constant π from mpmath
pi_value = mp.pi

# Negate π to get the result
result = -pi_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))