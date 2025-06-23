import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Square pi
pi_squared = mp.power(pi_val, 2)

# Divide by 16
result = pi_squared / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))