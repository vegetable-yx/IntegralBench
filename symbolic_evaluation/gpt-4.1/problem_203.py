import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Compute the sine of 1 radian
sin1 = mp.sin(1)

# Compute the cosine of 1 radian
cos1 = mp.cos(1)

# Calculate the result: 6 * sin(1) - 4 * cos(1)
result = 6 * sin1 - 4 * cos1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))