import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the result using Catalan's constant multiplied by 2
result = 2 * mp.catalan

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))