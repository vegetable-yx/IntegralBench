import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Multiply 506 by pi
result = 506 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))