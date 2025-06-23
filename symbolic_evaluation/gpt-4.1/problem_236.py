import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Multiply pi by 8
eight_pi = 8 * pi_val

# Divide the result by 3 to get the final value
result = eight_pi / 3

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))