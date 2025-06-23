import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/8
pi_over_8 = mp.pi / 8

# Calculate 1/4
one_fourth = mp.mpf(1) / 4

# Combine the terms: result = pi/8 - 1/4
result = pi_over_8 - one_fourth

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))