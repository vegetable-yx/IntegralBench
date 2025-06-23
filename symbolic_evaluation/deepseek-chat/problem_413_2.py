import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate the result as 506 * π
result = 506 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))