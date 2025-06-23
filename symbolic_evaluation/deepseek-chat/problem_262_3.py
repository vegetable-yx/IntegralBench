import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute sin(2) - sine of 2 radians
sin_val = mp.sin(2)

# Divide the result by 4
result = sin_val / 4

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))