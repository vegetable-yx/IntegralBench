import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Divide pi by 2 to get pi/2
result = pi_val / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))