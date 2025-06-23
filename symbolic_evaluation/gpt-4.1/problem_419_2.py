import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath constant
pi_val = mp.pi

# Square pi
pi_squared = pi_val ** 2

# Divide by 6 to get the result
result = pi_squared / 6

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))