import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of pi
pi_val = mp.pi

# Square the value of pi
pi_squared = pi_val ** 2

# Divide the squared pi by 4 to get the result
result = pi_squared / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))