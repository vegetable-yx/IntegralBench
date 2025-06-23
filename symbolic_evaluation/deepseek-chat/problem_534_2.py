import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Multiply pi by 2
two_pi = 2 * pi_val

# Compute the square root of (2 * pi)
result = mp.sqrt(two_pi)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))