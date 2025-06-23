import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute the constant π using mpmath
pi_value = mp.pi

# Divide π by 4 to get the result
result = pi_value / 4

# Print the result to 10 decimal places using mpmath's number string function
print(mp.nstr(result, n=10))