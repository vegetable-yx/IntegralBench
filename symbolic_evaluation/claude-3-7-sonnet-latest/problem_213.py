import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the sine of 1 radian
sin_value = mp.sin(1)

# Multiply the result by 2
result = 2 * sin_value

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))