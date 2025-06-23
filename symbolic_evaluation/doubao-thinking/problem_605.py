import mpmath as mp

# Set decimal places for internal precision to 15 to ensure 10 decimal places in output
mp.dps = 15

# Calculate the value of pi
pi_val = mp.pi

# Square the value of pi
pi_squared = pi_val ** 2

# Divide the squared pi by 16 to get the final result
result = pi_squared / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))