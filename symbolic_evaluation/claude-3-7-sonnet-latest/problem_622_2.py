import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant pi
pi_value = mp.pi

# Compute the expression: pi/4
result = pi_value / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))