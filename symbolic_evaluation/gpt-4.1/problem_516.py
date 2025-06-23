import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant pi divided by 2
pi_over_2 = mp.pi / 2

# Subtract 1 from pi/2
result = pi_over_2 - 1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))