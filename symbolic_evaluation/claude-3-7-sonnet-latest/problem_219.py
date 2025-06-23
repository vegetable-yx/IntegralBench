import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the sine of 1 radian
sin1 = mp.sin(1)

# Multiply the results to get the final value
result = sqrt2 * sin1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))