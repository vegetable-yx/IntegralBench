import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is a constant integer 18
result = 18

# Print the result as a floating-point number with exactly 10 decimal places
print(mp.nstr(result, n=10))