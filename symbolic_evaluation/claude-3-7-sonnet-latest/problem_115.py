import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi constant
pi_val = mp.pi

# Square the value of pi
pi_squared = pi_val ** 2

# Divide the squared pi by 8
result = pi_squared / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))