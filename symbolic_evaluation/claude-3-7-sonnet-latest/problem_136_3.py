import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi using mpmath constant
pi_val = mp.pi

# Multiply pi by 3
numerator = 3 * pi_val

# Divide by 2 to get the result
result = numerator / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))