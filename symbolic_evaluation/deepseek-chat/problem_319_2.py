import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi constant
pi_value = mp.pi

# Compute the expression: pi divided by 2
result = pi_value / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))