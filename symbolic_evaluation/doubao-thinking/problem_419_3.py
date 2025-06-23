import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi using mpmath's constant
pi_val = mp.pi

# Square pi to get pi squared
pi_squared = pi_val ** 2

# Divide by 6 to get the final result
result = pi_squared / 6

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))