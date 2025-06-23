import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute the sine of 1 radian
result = mp.sin(1)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))