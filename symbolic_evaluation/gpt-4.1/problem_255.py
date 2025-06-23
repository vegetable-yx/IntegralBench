import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the result: -3 * π
result = -3 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))