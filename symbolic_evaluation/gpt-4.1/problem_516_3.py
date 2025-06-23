import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi/2
pi_over_2 = mp.pi / 2

# Subtract 1
result = pi_over_2 - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))