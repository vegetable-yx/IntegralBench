import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the sine of 2 radians
sin_val = mp.sin(2)

# Divide the result by 4
result = sin_val / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))