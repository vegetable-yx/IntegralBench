import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is π/2
# Compute pi divided by 2
result = mp.pi / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))