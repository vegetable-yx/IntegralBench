import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Square the value of pi
result = pi_val ** 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))