import mpmath as mp

# Set internal precision to 15 decimal places for accurate computations
mp.dps = 15

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Calculate pi divided by 3
pi_over_3 = mp.pi / 3

# Combine the results: sqrt(3) - pi/3
result = sqrt3 - pi_over_3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))