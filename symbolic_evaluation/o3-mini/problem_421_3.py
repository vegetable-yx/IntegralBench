import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute sine of 1 radian
result = mp.sin(1)

# Print the result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))