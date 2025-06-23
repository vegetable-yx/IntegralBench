import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi divided by 30
result = mp.pi / 30

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))