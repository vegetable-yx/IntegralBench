import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the sine of 1 radian
result = mp.sin(1)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))