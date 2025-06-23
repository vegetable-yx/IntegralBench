import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the expression: π/8
result = mp.pi / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))