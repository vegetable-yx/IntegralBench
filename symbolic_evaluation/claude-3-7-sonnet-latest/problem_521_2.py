import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the argument for the logarithm
x = mp.mpf(3)

# Compute the natural logarithm of 3
result = mp.log(x)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))