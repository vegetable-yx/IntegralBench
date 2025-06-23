import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute the constant pi
pi_value = mp.pi

# Calculate pi/2
pi_over_2 = pi_value / 2

# Evaluate the expression: 2 - pi/2
result = 2 - pi_over_2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))