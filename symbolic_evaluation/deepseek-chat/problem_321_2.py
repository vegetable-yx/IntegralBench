import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Divide pi by 2 to obtain the result
result = pi_val / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))