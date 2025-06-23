import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is 506 * pi
# Compute the product of 506 and pi
result = 506 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))