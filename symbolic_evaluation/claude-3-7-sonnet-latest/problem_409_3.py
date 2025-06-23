import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Compute the value of π
pi_value = mp.pi

# Calculate π divided by 4
result = pi_value / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))