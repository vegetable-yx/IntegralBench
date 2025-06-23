import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the argument for the logarithm
x = 2

# Compute the natural logarithm of 2
result = mp.log(x)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))