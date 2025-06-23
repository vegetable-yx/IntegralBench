import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Calculate π divided by 4
pi_over_4 = mp.pi / 4

# Sum the two components
result = ln3 + pi_over_4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))