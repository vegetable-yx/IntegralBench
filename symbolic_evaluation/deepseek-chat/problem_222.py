import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 3 times pi
three_pi = 3 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(three_pi, n=10))