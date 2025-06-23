import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the argument (1 radian)
x = mp.mpf(1)

# Compute the sine of 1 radian
result = mp.sin(x)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))