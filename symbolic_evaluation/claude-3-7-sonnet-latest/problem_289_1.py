import mpmath as mp

# Set internal decimal places for computation to 15 for accuracy
mp.dps = 15

# Compute pi using mpmath's built-in constant
pi_value = mp.pi

# Divide pi by 32 to get the result
result = pi_value / 32

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))